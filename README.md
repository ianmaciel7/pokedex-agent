# pokedex-agent

A hands-on Pokédex-style AI agent built with Google ADK and PokéAPI.

I created this project to learn how Google ADK works in practice: how to define
agents, connect tools, split responsibilities across specialist sub-agents, run
the project locally, and handle real API data inside an agent workflow.

## ADK topics used

This repository is both a working agent and a study project. The ADK topics used are:

- [x] Root agent entry point with `root_agent`.
- [x] ADK `App` wiring.
- [x] Orchestrator agents.
- [x] Specialist sub-agents.
- [x] Sub-agent delegation.
- [x] Function tools for PokéAPI data.
- [x] Shared model configuration.
- [x] ADK plugin callbacks for model and tool errors.
- [x] ADK Web.
- [x] ADK CLI runs.

## Requirements

- Python 3.12+
- `uv`
- A Gemini API key for ADK model calls

## Language agents

The package exposes two orchestrator agents:

- `english_agent` answers in English.
- `pt_br_agent` answers in Brazilian Portuguese.

`root_agent` remains available as the default ADK entry point and points to `english_agent`.

## Project structure

This project is organized as a single ADK agent package in `pokedex_agent/`.
That directory contains `agent.py`, which exports the default `root_agent`.

- `pokedex_agent/agent.py` wires the orchestrator agents and ADK app.
- `pokedex_agent/factory.py` contains shared agent factory helpers.
- `pokedex_agent/sub_agents/` contains specialist sub-agents.
- `pokedex_agent/tools/` contains PokéAPI tool wrappers grouped by domain.
- `AGENTS.md` contains coding-agent instructions, project conventions, and checks.

## Agent flow

The orchestrator receives the user question, selects the best specialist
sub-agent, and that sub-agent calls the PokéAPI through its domain tools.

```mermaid
flowchart TD
    user[User question] --> entry[ADK entry point<br/>root_agent]
    entry --> app[ADK App<br/>pokedex_agent]
    app --> english[english_agent<br/>default orchestrator]
    app -. optional .-> portuguese[pt_br_agent<br/>Brazilian Portuguese orchestrator]

    english --> route{Orchestrator<br/>identifies topic}
    portuguese --> route

    route --> pokemon[Delegate to pokemon_agent<br/>stats, species, forms]
    route --> moves[Delegate to move_agent<br/>moves and battle mechanics]
    route --> abilities[Delegate to ability_agent<br/>abilities and type matchups]
    route --> items[Delegate to item_agent<br/>items and berries]
    route --> world[Delegate to world_agent<br/>locations and encounters]
    route --> meta[Delegate to meta_agent<br/>versions, evolution, contests]

    pokemon --> tools[Sub-agent calls<br/>domain tools]
    moves --> tools
    abilities --> tools
    items --> tools
    world --> tools
    meta --> tools

    tools --> pokebase[pokebase]
    pokebase --> pokeapi[PokéAPI call]
    pokeapi --> tools
    tools --> answer[Formatted answer<br/>data plus image when available]
    answer --> user

    tools -. errors .-> plugin[GlobalErrorPlugin]
    plugin --> answer
```

## Setup

Install dependencies from the project root:

```sh
uv sync
```

Copy the example environment file and add your API key:

```sh
cp .env.example .env
```

Use `MODEL_PROVIDER=google` for Gemini API calls, `MODEL_PROVIDER=nvidia` for
NVIDIA NIM, or `MODEL_PROVIDER=local` for a local LiteLLM/Ollama model.

The SDK accepts `GOOGLE_API_KEY` or `GEMINI_API_KEY`. If both are set,
`GOOGLE_API_KEY` takes precedence.

For NVIDIA NIM, use `.env.nvidia`:

```env
MODEL_PROVIDER=nvidia
NVIDIA_NIM_API_KEY=REPLACE_WITH_YOUR_NVIDIA_NIM_API_KEY
NVIDIA_MODEL=nvidia_nim/deepseek-ai/deepseek-v4-flash
```

Do not paste real API keys into chat or commit them to git. Fill the key locally
in `.env.nvidia`, which is ignored by git.

If ADK returns `_ResourceExhaustedError`, the selected model has exhausted its
quota or rate limit. Wait and retry, switch to `MODEL_PROVIDER=local`, or use a
Gemini API key/project with available quota.

## Run with ADK

Run the ADK web UI from the project root:

```sh
uv run adk web pokedex_agent
```

For a one-shot CLI run:

```sh
uv run adk run pokedex_agent "Tell me about Pikachu"
```

## Development checks

Run Ruff before finishing changes:

```sh
uv run ruff check pokedex_agent
```

Format code with:

```sh
uv run ruff format pokedex_agent
```

After changing agent wiring, imports, exports, or factories, run:

```sh
uv run python -c "import pokedex_agent.agent; from pokedex_agent.sub_agents import create_all_sub_agents; print(len(create_all_sub_agents()))"
```
