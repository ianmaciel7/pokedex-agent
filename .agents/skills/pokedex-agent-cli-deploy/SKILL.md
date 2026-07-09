---
name: pokedex-agent-cli-deploy
description: Deploy, inspect, update, or delete the local pokedex-agent Google ADK package on Google Cloud using the google-agents-cli-deploy CLI. Use when Codex is asked to create, add, deploy, redeploy, list, observe, or remove a Pokédex agent deployment on Agent Runtime or Agent Engine, with Agent Runtime / Agent Engine as the default target.
---

# Pokédex Agent CLI Deploy

## Original Skill Reference

This is the Pokédex-local adaptation of the original
`google-agents-cli-deploy` workflow. Keep the generic CLI guidance in
`references/google-agents-cli-deploy.md` as the source reference, then apply the
repository-specific rules in this file.

## Overview

Use this skill to operate cloud deployments for the `pokedex-agent` Google ADK
package. Drive all deployment lifecycle actions through `google-agents-cli-deploy`
unless the CLI is missing or its own help output proves a different command is
required.

Default to Agent Runtime / Agent Engine when the user does not specify a target.
Treat create, deploy, update, list, describe, logs, and delete as cloud operations
that must be verified before and after the CLI call.

## Workflow

1. Confirm the repository looks like this package:
   - `pyproject.toml` project name is `pokedex-agent`.
   - `pokedex_agent/agent.py` exports the ADK entry point.
   - `pokedex_agent` imports locally without syntax errors.
2. Check credentials and configuration before cloud calls:
   - Run `gcloud auth list` when Google Cloud auth is relevant.
   - Prefer explicit project and region values from user input, environment,
     `gcloud config`, or a repo deployment config.
   - Do not invent project IDs, regions, service accounts, image names, or
     resource IDs.
3. Inspect the installed CLI before using it:
   - Try `google-agents-cli-deploy --help`.
   - If that fails, try `uv run google-agents-cli-deploy --help`.
   - If still missing, report that the CLI is unavailable and ask whether to add
     or install the correct dependency.
4. Use the bundled scripts for the requested lifecycle action when they fit:
   - `scripts/deploy.sh` for create, update, or redeploy.
   - `scripts/delete-deploy.sh` for deletion.
   - Pass additional CLI-specific flags after `--`.
5. Parse and report the resulting deployment name, resource ID, console URL,
   endpoint, region, and project when the CLI outputs them.
6. Verify the operation with the CLI, not memory:
   - After create/update, run the relevant list or describe command.
   - After delete, run the relevant list or describe command and confirm the
     resource is gone or marked deleting.

## Safety Rules

- Ask before deleting a cloud deployment unless the user explicitly requested
  deletion in the current turn.
- Never delete more than one deployment from a fuzzy name. List matches and ask
  for the exact resource when ambiguity remains.
- Never commit or print API keys. Local `.env` files are sensitive.
- Do not deploy with placeholder credentials, placeholder project IDs, or a
  guessed service account.
- If a command fails due to authentication, use the `gcloud-auth-verification`
  skill if available.

## Pokédex Preflight

Run these focused checks before deployment when files changed or when the user
asks for a deploy from the current checkout:

```sh
uv run ruff check pokedex_agent
uv run python -c "import pokedex_agent.agent; from pokedex_agent.sub_agents import create_all_sub_agents; print(len(create_all_sub_agents()))"
```

If runtime behavior or ADK startup changed, run a focused ADK check when
credentials are available:

```sh
uv run adk run pokedex_agent "Tell me about Pikachu"
```

## Bundled Scripts

Deploy with the default Agent Engine target:

```sh
scripts/deploy.sh --name pokedex-agent-dev --project PROJECT_ID --region REGION
```

Delete a deployment only after identifying exactly one resource:

```sh
scripts/delete-deploy.sh --deployment DEPLOYMENT_ID --project PROJECT_ID --region REGION
```

Use `--target agent-runtime` when the user explicitly wants Agent Runtime. Use
`--dry-run` to print the resolved command without calling Google Cloud.

## CLI Guidance

Read `references/google-agents-cli-deploy.md` when planning or executing an
actual create, update, inspect, logs, or delete operation. Use the reference as a
pattern, then prefer the installed CLI's `--help` output over any remembered
syntax.
