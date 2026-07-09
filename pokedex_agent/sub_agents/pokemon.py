"""Sub-agent for core Pokémon data."""

from google.adk.agents.llm_agent import Agent

from pokedex_agent.factory import create_sub_agent
from pokedex_agent.tools.pokemon import pokemon_tools


def create_pokemon_agent() -> Agent:
    return create_sub_agent("pokemon", pokemon_tools)


pokemon_agent = create_pokemon_agent()
