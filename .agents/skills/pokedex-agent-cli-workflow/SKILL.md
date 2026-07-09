---
name: pokedex-agent-cli-workflow
description: Plan or run the full development workflow for the local pokedex-agent Google ADK package, from code changes and scaffold through evals, observability, and deployment. Use when Codex is asked for an end-to-end Pokédex ADK workflow, lifecycle, or recommended command sequence.
---

# Pokédex Agent CLI Workflow

## Original Skill Reference

This is the Pokédex-local adaptation of the original
`google-agents-cli-workflow` skill. Keep the generic CLI guidance in
`references/google-agents-cli-workflow.md` as the source reference, then apply
the repository-specific rules in this file.

## Overview

Use this skill to coordinate end-to-end development for the `pokedex-agent`
Google ADK package. Drive lifecycle work through the narrower local skills when
the request becomes specific, and discover installed Google Agents CLI command
surfaces before assuming exact syntax.

Treat code changes, evals, observability, and deployment as separate phases with
their own validation. Keep Agent Runtime / Agent Engine as the default cloud
target when the user does not specify one.

## Workflow

1. Confirm the repository looks like this package:
   - `pyproject.toml` project name is `pokedex-agent`.
   - `pokedex_agent/agent.py` exports the ADK entry point.
   - `pokedex_agent` imports locally without syntax errors.
2. Identify the requested lifecycle phase:
   - Code changes: use `pokedex-agent-cli-adk-code`.
   - Project structure: use `pokedex-agent-cli-scaffold`.
   - Evals: use `pokedex-agent-cli-eval`.
   - Deployment: use `pokedex-agent-cli-deploy`.
   - Logs, traces, and runtime status: use `pokedex-agent-cli-observability`.
3. Inspect installed CLI help before using commands:
   - Try the phase-specific `google-agents-cli-* --help`.
   - If that fails, try `uv run google-agents-cli-* --help`.
   - If neither exists, use the repository's local `uv run adk --help` surface
     when applicable.
4. Run local quality gates before runtime or cloud actions.
5. Parse and report the command used, result, skipped checks, and any missing
   credentials or unavailable CLI packages.
6. For cloud operations, verify project, region, target runtime, and resource ID
   before and after the CLI call.

## Safety Rules

- Never commit or print API keys, tokens, credentials, or local `.env` files.
- Do not invent project IDs, regions, service accounts, image names, deployment
  IDs, trace IDs, or resource IDs.
- Ask before deleting a cloud deployment unless deletion was explicitly
  requested in the current turn.
- Prefer the installed CLI's help output over remembered syntax.

## Pokédex Preflight

Run these focused checks before runtime or cloud actions when files changed:

```sh
uv run ruff check pokedex_agent
uv run python -c "import pokedex_agent.agent; from pokedex_agent.sub_agents import create_all_sub_agents; print(len(create_all_sub_agents()))"
```

If runtime behavior or ADK startup changed, run a focused ADK check when
credentials are available:

```sh
uv run adk run pokedex_agent "Tell me about Pikachu"
```

## CLI Guidance

Read `references/google-agents-cli-workflow.md` when planning or executing a
multi-phase workflow that spans code, scaffold, evals, observability, or
deployment. Use the reference as a pattern, then prefer the installed CLI's
`--help` output over any remembered syntax.
