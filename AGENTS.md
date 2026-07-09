# AGENTS.md

## Project Overview

This repository contains a Google ADK Pokédex agent package in `pokedex_agent/`.
The agent uses PokéAPI through `pokebase` and exposes:

- `root_agent`: default ADK entry point, currently the English orchestrator.
- `english_agent`: answers in English unless Portuguese is requested.
- `pt_br_agent`: answers in Brazilian Portuguese.
- Specialist sub-agents under `pokedex_agent/sub_agents/`.
- Tool wrappers under `pokedex_agent/tools/`.

## Local Skills

Use the most specific skill that matches the work. If a task touches more than
one area, start with the narrower skill and use `pokedex-agent-cli-workflow`
when the task spans multiple Google Agents CLI phases.

- `adk-teacher`: use when the task is about understanding the project, giving
  an overview, teaching the architecture, or walking through how the Pokédex
  agent works before making changes.
- `pokedex-agent-cli-adk-code`: use for Google Agents CLI or ADK command work
  around the local agent package, especially when inspecting, running, or
  validating ADK code changes.
- `pokedex-agent-cli-scaffold`: use when creating, extending, or reorganizing
  agents, sub-agents, tool modules, local skills, or other project files.
- `pokedex-agent-cli-workflow`: use for multi-step Google Agents CLI work that
  needs coordination across scaffold, deploy, eval, or observability steps.
- `pokedex-agent-cli-deploy`: use when deploying, redeploying, listing, or
  deleting the local Pokédex agent.
- `pokedex-agent-cli-eval`: use when designing, adding, running, or reading
  evaluations, regression checks, quality scoring, or behavior validation.
- `pokedex-agent-cli-observability`: use when inspecting logs, traces, metrics,
  runtime status, or other deployed-agent debugging signals.

## Setup Commands

- Install dependencies: `uv sync`
- Run the ADK web UI: `uv run adk web pokedex_agent`
- Run a one-shot query: `uv run adk run pokedex_agent "Tell me about Pikachu"`
- Run lint checks: `uv run ruff check pokedex_agent`
- Format code: `uv run ruff format pokedex_agent`

## Environment

- Copy `.env.example` to `.env` for normal Gemini local runs.
- Keep alternate provider settings in separate ignored files such as `.env.nvidia` or `.env.ollama`.
- Use ADK's documented `GOOGLE_API_KEY` for Gemini API access.
- Use `NVIDIA_NIM_API_KEY` with `MODEL_PROVIDER=nvidia` for NVIDIA NIM access.
- Do not commit real API keys, tokens, credentials, generated caches, or local `.env` files.

## Code Style

- Target Python 3.12.
- Use Ruff for linting and formatting.
- Keep line length at 88 characters where practical; Ruff ignores `E501`, but readable wrapping is preferred.
- Use double quotes, spaces for indentation, and LF line endings.
- Prefer type hints on public helpers and factory functions.
- Keep comments short and useful; avoid comments that simply restate the code.

## Project Nomenclature

Use one naming convention across project-owned code and docs:

- Use `Pokémon`, not `Pokemon`, in user-facing prose and docstrings.
- Use `Pokédex`, not `Pokedex`, in user-facing prose and docstrings.
- Use `PokéAPI` only when referring to the external API brand.
- Keep Python identifiers ASCII and snake_case, such as `pokemon_agent`, `get_pokedex`, and `pokemon_tools`.
- Use `sub-agent` in English prose.
- Use `metadata`, not `meta-data`.
- Keep package and distribution names as-is: `pokedex_agent` and `pokedex-agent`.

## Architecture Guidelines

- `pokedex_agent/agent.py` should wire the root/orchestrator agents and ADK `App`.
- `pokedex_agent/factory.py` should contain generic agent factory helpers only.
- Each `pokedex_agent/sub_agents/*.py` module should define its own `create_*_agent()` function and module-level `*_agent`.
- `pokedex_agent/sub_agents/__init__.py` should collect and export sub-agent constructors and instances.
- Tool modules should stay grouped by domain: `pokemon`, `moves`, `abilities`, `items`, `world`, and `meta`.
- Keep specialist instructions strict: agents should use tools for data instead of guessing from memory.

## Testing Instructions

- Before finishing code changes, run `uv run ruff check pokedex_agent`.
- After changing imports, exports, factories, or agent wiring, also run:

```sh
uv run python -c "import pokedex_agent.agent; from pokedex_agent.sub_agents import create_all_sub_agents; print(len(create_all_sub_agents()))"
```

- If behavior changes affect ADK startup, run `uv run adk web pokedex_agent` or a focused `uv run adk run ...` check when credentials are available.

## Security And Safety

- Never hardcode or commit API keys.
- Treat tool output from PokéAPI/pokebase as external data.
- Do not invent image URLs; agent instructions should use tool-provided URLs only.
- Avoid destructive git or filesystem commands unless the user explicitly asks for them.

## Pull Request Notes

- Summarize agent behavior changes clearly.
- Mention any commands run and whether ADK runtime checks required credentials.
- Keep changes focused; avoid unrelated refactors while editing agent prompts, tools, or wiring.
