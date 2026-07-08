"""Sub-agent for core Pokémon data."""

from google.adk.agents.llm_agent import Agent

from pokedex_agent.factory import create_sub_agent
from pokedex_agent.tools.pokemon import pokemon_tools


def create_pokemon_agent() -> Agent:
    return create_sub_agent(
        name="pokemon_agent",
        description=(
            "Handles queries about Pokémon themselves: base stats, types, abilities, moves, "
            "species details, forms, colors, habitats, shapes, egg groups, natures, growth rates, "
            "genders, generations, characteristics, Pokédexes, and Pokéathlon stats."
        ),
        instruction=(
            "You are a Pokémon data specialist. "
            "Use the available tools to look up accurate data about Pokémon and return clear, "
            "well-formatted answers. "
            "Always use the tool — never guess stats or data from memory."
        ),
        tools=pokemon_tools,
    )


pokemon_agent = create_pokemon_agent()
