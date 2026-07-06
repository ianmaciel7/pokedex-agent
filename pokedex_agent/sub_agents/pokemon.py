from pokedex_agent.model_config import get_model
"""Sub-agent for core Pokémon data."""

from google.adk.agents.llm_agent import Agent
from pokedex_agent.tools.pokemon import pokemon_tools

pokemon_agent = Agent(
    model=get_model(),
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
