# pokedex-agent
A hands-on Pokédex-style AI agent built with Google ADK and PokeAPI to explore agent tools and API integration.

## Language agents

The package exposes two orchestrator agents:

- `english_agent` answers in English.
- `pt_br_agent` answers in Brazilian Portuguese.

`root_agent` remains available as the default ADK entry point and points to `english_agent`.
