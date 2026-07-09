"""Sub-agent for core Pokémon data."""

from google.adk.agents.llm_agent import Agent

from pokedex_agent.factory import create_sub_agent
from pokedex_agent.tools.pokemon import pokemon_tools


def create_pokemon_agent() -> Agent:
    return create_sub_agent(
        name="pokemon_agent",
        description=(
            "Handles core Pokémon data queries: base stats, types, abilities, moves, "
            "species details, forms, colors, habitats, shapes, egg groups, natures, growth rates, "
            "genders, generations, characteristics, Pokédex entries, and Pokéathlon stats."
        ),
        instruction=(
            "You are the Pokémon data specialist. "
            "Use the available tools to retrieve accurate Pokémon data and return clear, "
            "well-formatted answers. "
            "Always use tools for factual data instead of guessing from memory."
        ),
        tools=pokemon_tools,
    )


pokemon_agent = create_pokemon_agent()
