#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Delete a Pokédex ADK cloud deployment with google-agents-cli-deploy.

Usage:
  delete-deploy.sh --deployment DEPLOYMENT_ID [--project PROJECT_ID]
                   [--region REGION] [--target agent-engine|agent-runtime]
                   [--yes] [--dry-run] [-- EXTRA_CLI_FLAGS...]

Defaults:
  --target agent-engine
  --project from gcloud config when available
  --region from gcloud config compute/region when available

Examples:
  scripts/delete-deploy.sh --deployment pokedex-agent-dev --project my-project --region us-central1
  scripts/delete-deploy.sh --deployment 123456789 --yes -- --force
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
deployment=""
project="${GOOGLE_CLOUD_PROJECT:-${GOOGLE_PROJECT:-}}"
region="${GOOGLE_CLOUD_REGION:-${GOOGLE_REGION:-}}"
assume_yes=0
dry_run=0
extra_args=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --deployment|--id|--name)
      deployment="${2:-}"
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
    --yes|-y)
      assume_yes=1
      shift
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

[[ -n "$deployment" ]] || die "--deployment is required"
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
  delete
  "$deployment"
  --project "$project"
  --region "$region"
)

if [[ ${#extra_args[@]} -gt 0 ]]; then
  cmd+=("${extra_args[@]}")
fi

echo "Deleting deployment $deployment from $target in $project/$region"
printf 'Command:'
printf ' %q' "${cmd[@]}"
printf '\n'

if [[ "$dry_run" -eq 1 ]]; then
  exit 0
fi

if [[ "$assume_yes" -ne 1 ]]; then
  read -r -p "Type the deployment ID/name to confirm deletion: " confirmation
  [[ "$confirmation" == "$deployment" ]] || die "Confirmation did not match; deletion cancelled"
fi

"${cmd[@]}"
