---
name: pokedex-agent-cli-adk-code
description: Edit or generate Google ADK Python code for the local Pokédex agent package using project conventions, first-party ADK documentation, and installed CLI help. Use when Codex is asked to change agent code, tools, orchestration, callbacks, model configuration, or sub-agent wiring.
---

# Pokédex Agent CLI ADK Code

## Original Skill Reference

This is the Pokédex-local adaptation of the original
`google-agents-cli-adk-code` skill. Keep the generic CLI guidance in
`references/google-agents-cli-adk-code.md` as the source reference, then apply
the repository-specific rules in this file. For agent wiring and definition
patterns, also read `references/agent-definition.md` before editing
`pokedex_agent/agent.py`, `pokedex_agent/factory.py`, or
`pokedex_agent/sub_agents/*.py`.

## Overview

Use this skill when changing ADK Python code in `pokedex_agent/`.
Drive ADK agent, tool, orchestration, callback, and model configuration work
through the repository's existing patterns and the installed ADK help output.
Prefer official ADK documentation and `adk --help` output over remembered
syntax or stale examples.

Treat code changes that alter imports, exports, factories, or agent wiring as
runtime-affecting changes that require focused validation before finishing.

## Workflow

1. Confirm the repository looks like this package:
   - `pyproject.toml` project name is `pokedex-agent`.
   - `pokedex_agent/agent.py` exports the ADK entry point.
   - `pokedex_agent` imports locally without syntax errors.
2. Inspect the existing module before editing and follow the local package
   layout for factories, sub-agents, tools, model configuration, and the agent
   definition patterns in `references/agent-definition.md`.
3. Inspect installed command help before relying on any CLI syntax:
   - Try `google-agents-cli-adk-code --help`.
   - If that fails, try `UV_CACHE_DIR=/tmp/uv-cache uv run google-agents-cli-adk-code --help`.
   - If neither exists, use `UV_CACHE_DIR=/tmp/uv-cache uv run adk --help`.
4. Keep specialist instructions strict: agents should use tools for data instead
   of guessing from memory, and orchestrators should delegate rather than
   answering factual Pokémon questions themselves.
5. After import, export, factory, or wiring changes, run the focused checks in
   the Pokédex Preflight section.
6. Prefer native ADK-friendly tool returns over custom wrapper layers:
   - Return plain JSON-serializable dict payloads from tool functions.
   - Prefer `output` and `error` keys for tool responses.
   - If a response schema is helpful, let the tool module own its response
     model directly instead of routing through shared builder helpers.
   - Prefer `TypedDict` payload schemas over broad `object`, `Any`, or
     `JsonValue` annotations.
   - Keep `Any` out of function arguments unless there is no safer typing
     option; Ruff should flag new `Any` argument annotations with `ANN401`.

## Safety Rules

- Never hardcode or print API keys. Local `.env` files are sensitive.
- Do not invent image URLs; use tool-provided URLs only.
- Keep Python identifiers ASCII, but use `Pokémon`, `Pokédex`, and `PokéAPI`
  in user-facing prose and docstrings.
- Avoid broad rewrites while editing agent prompts, tools, callbacks, or wiring.
- Avoid introducing shared response-builder wrappers for simple tool payloads
  when a direct schema instance or direct dict return is clearer.

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
