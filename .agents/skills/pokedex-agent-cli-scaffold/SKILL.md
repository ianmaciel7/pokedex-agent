---
name: pokedex-agent-cli-scaffold
description: Create, extend, or reorganize the local pokedex-agent Google ADK project scaffold using project conventions and Google Agents CLI discovery. Use when Codex is asked to scaffold Pokédex agents, sub-agents, tool modules, local skills, or project files.
---

# Pokédex Agent CLI Scaffold

## Original Skill Reference

This is the Pokédex-local adaptation of the original
`google-agents-cli-scaffold` skill. Keep the generic CLI guidance in
`references/google-agents-cli-scaffold.md` as the source reference, then apply
the repository-specific rules in this file.

## Overview

Use this skill to create or extend ADK project structure while matching this
repository's conventions. Drive scaffolding through `google-agents-cli-scaffold`
when it is installed, or by manually creating files that match the established
Pokédex package layout.

Treat generated structure as project-owned code: keep it focused, importable,
and aligned with the existing naming rules.

## Workflow

1. Confirm the repository looks like this package:
   - `pyproject.toml` project name is `pokedex-agent`.
   - `pokedex_agent/agent.py` exports the ADK entry point.
   - Existing sub-agents and tools are under `pokedex_agent/`.
2. Inspect the installed scaffold CLI before using it:
   - Try `google-agents-cli-scaffold --help`.
   - If that fails, try `uv run google-agents-cli-scaffold --help`.
   - If neither exists, scaffold manually using the repository layout.
3. Add only the files needed for the requested feature and follow the existing
   package layout for root wiring, factories, sub-agents, tools, and local
   skills.
4. Update exports when adding sub-agent constructors or instances.
5. Run the focused checks in the Pokédex Preflight section.

## Safety Rules

- Never scaffold files containing real API keys, tokens, credentials, or local
  `.env` values.
- Keep Python identifiers ASCII and snake_case.
- Use `Pokémon`, `Pokédex`, `PokéAPI`, and `sub-agent` in user-facing prose.
- Do not create unrelated boilerplate, generated caches, or broad refactors.

## Pokédex Preflight

Run Ruff after scaffolded code changes:

```sh
uv run ruff check pokedex_agent
```

Run the import/wiring check after changing exports, factories, or agent wiring:

```sh
uv run python -c "import pokedex_agent.agent; from pokedex_agent.sub_agents import create_all_sub_agents; print(len(create_all_sub_agents()))"
```

## CLI Guidance

Read `references/google-agents-cli-scaffold.md` when planning or executing
project, sub-agent, tool, or skill scaffolding. Use the reference as a pattern,
then prefer installed CLI help output over remembered syntax.
