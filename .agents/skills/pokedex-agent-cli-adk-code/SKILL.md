---
name: pokedex-agent-cli-adk-code
description: Edit or generate Google ADK Python code for the local pokedex-agent package using project conventions and Google Agents CLI discovery. Use when Codex is asked to change Pokédex agent code, tools, orchestration, callbacks, model configuration, or sub-agent wiring.
---

# Pokédex Agent CLI ADK Code

## Original Skill Reference

This is the Pokédex-local adaptation of the original
`google-agents-cli-adk-code` skill. Keep the generic CLI guidance in
`references/google-agents-cli-adk-code.md` as the source reference, then apply
the repository-specific rules in this file.

## Overview

Use this skill when changing ADK Python code in `pokedex_agent/`.
Drive ADK agent, tool, orchestration, callback, and model configuration work
through the repository's existing patterns. Use Google Agents CLI or ADK help
output for command behavior instead of remembered syntax.

Treat code changes that alter imports, exports, factories, or agent wiring as
runtime-affecting changes that require focused validation before finishing.

## Workflow

1. Confirm the repository looks like this package:
   - `pyproject.toml` project name is `pokedex-agent`.
   - `pokedex_agent/agent.py` exports the ADK entry point.
   - `pokedex_agent` imports locally without syntax errors.
2. Inspect the existing module before editing and follow the local package
   layout for factories, sub-agents, tools, and model configuration.
3. Inspect installed command help before relying on a CLI operation:
   - Try `google-agents-cli-adk-code --help`.
   - If that fails, try `uv run google-agents-cli-adk-code --help`.
   - If neither exists, use `uv run adk --help` for available ADK commands.
4. Keep specialist instructions strict: agents should use tools for data instead
   of guessing from memory.
5. After import, export, factory, or wiring changes, run the focused checks in
   the Pokédex Preflight section.

## Safety Rules

- Never hardcode or print API keys. Local `.env` files are sensitive.
- Do not invent image URLs; use tool-provided URLs only.
- Keep Python identifiers ASCII, but use `Pokémon`, `Pokédex`, and `PokéAPI` in
  user-facing prose and docstrings.
- Avoid broad rewrites while editing agent prompts, tools, callbacks, or wiring.

## Pokédex Preflight

Run these focused checks before finishing code changes:

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

Read `references/google-agents-cli-adk-code.md` when planning or executing
actual ADK code, tool, orchestration, callback, or runtime behavior work. Use
the reference as a pattern, then prefer installed CLI and ADK help output over
any remembered syntax.
