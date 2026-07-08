#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Deploy the Pokédex ADK agent with google-agents-cli-deploy.

Usage:
  deploy.sh --name NAME [--project PROJECT_ID] [--region REGION]
            [--target agent-engine|agent-runtime] [--app pokedex_agent]
            [--entry-point MODULE:OBJECT] [--dry-run] [-- EXTRA_CLI_FLAGS...]

Defaults:
  --target agent-engine
  --app pokedex_agent
  --project from gcloud config when available
  --region from gcloud config compute/region when available

Examples:
  scripts/deploy.sh --name pokedex-agent-dev --project my-project --region us-central1
  scripts/deploy.sh --name pokedex-agent-dev -- --env-vars-file .env.deploy
USAGE
}

die() {
  echo "ERROR: $*" >&2
  exit 1
}

gcloud_value() {
  local key="$1"
  if command -v gcloud >/dev/null 2>&1; then
    gcloud config get-value "$key" 2>/dev/null || true
  fi
}

resolve_cli() {
  if command -v google-agents-cli-deploy >/dev/null 2>&1; then
    CLI_CMD=(google-agents-cli-deploy)
    return
  fi

  if command -v uv >/dev/null 2>&1 && uv run google-agents-cli-deploy --help >/dev/null 2>&1; then
    CLI_CMD=(uv run google-agents-cli-deploy)
    return
  fi

  die "google-agents-cli-deploy was not found. Install the CLI or add it to this project's uv environment."
}

target="agent-engine"
app="pokedex_agent"
name=""
project="${GOOGLE_CLOUD_PROJECT:-${GOOGLE_PROJECT:-}}"
region="${GOOGLE_CLOUD_REGION:-${GOOGLE_REGION:-}}"
entry_point=""
dry_run=0
extra_args=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --name)
      name="${2:-}"
      shift 2
      ;;
    --project)
      project="${2:-}"
      shift 2
      ;;
    --region)
      region="${2:-}"
      shift 2
      ;;
    --target)
      target="${2:-}"
      shift 2
      ;;
    --app)
      app="${2:-}"
      shift 2
      ;;
    --entry-point)
      entry_point="${2:-}"
      shift 2
      ;;
    --dry-run)
      dry_run=1
      shift
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    --)
      shift
      extra_args=("$@")
      break
      ;;
    *)
      die "Unknown argument: $1"
      ;;
  esac
done

[[ -n "$name" ]] || die "--name is required"
[[ "$target" == "agent-engine" || "$target" == "agent-runtime" ]] || die "--target must be agent-engine or agent-runtime"

if [[ -z "$project" ]]; then
  project="$(gcloud_value project)"
fi

if [[ -z "$region" ]]; then
  region="$(gcloud_value compute/region)"
fi

[[ -n "$project" ]] || die "--project is required or must be configured in gcloud"
[[ -n "$region" ]] || die "--region is required or must be configured in gcloud"

declare -a CLI_CMD
resolve_cli

cmd=(
  "${CLI_CMD[@]}"
  "$target"
  deploy
  --project "$project"
  --region "$region"
  --app "$app"
  --display-name "$name"
)

if [[ -n "$entry_point" ]]; then
  cmd+=(--entry-point "$entry_point")
fi

if [[ ${#extra_args[@]} -gt 0 ]]; then
  cmd+=("${extra_args[@]}")
fi

echo "Deploying $app to $target in $project/$region as $name"
printf 'Command:'
printf ' %q' "${cmd[@]}"
printf '\n'

if [[ "$dry_run" -eq 1 ]]; then
  exit 0
fi

"${cmd[@]}"
