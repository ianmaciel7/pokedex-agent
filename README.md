# pokedex-agent
A hands-on Pokédex-style AI agent built with Google ADK and PokeAPI to explore agent tools and API integration.

## Language agents

The package exposes two orchestrator agents:

- `english_agent` answers in English.
- `pt_br_agent` answers in Brazilian Portuguese.

`root_agent` remains available as the default ADK entry point and points to `english_agent`.

## Run with ADK

This project is organized as a single ADK agent package in `pokedex_agent/`.
That directory contains `agent.py`, which exports the default `root_agent`.

Run the ADK web UI from the project root:

```sh
adk web pokedex_agent
```

For a one-shot CLI run:

```sh
adk run pokedex_agent "Tell me about Pikachu"
```
