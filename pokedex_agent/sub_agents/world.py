"""Sub-agent for locations, encounters, and regions."""

from google.adk.agents.llm_agent import Agent

from pokedex_agent.factory import create_sub_agent
from pokedex_agent.tools.world import world_tools


def create_world_agent() -> Agent:
    return create_sub_agent(
        name="world_agent",
        description=(
            "Handles Pokémon world queries: locations and their subareas, wild encounter rates, "
            "encounter methods, encounter conditions, game regions, and Pal Park areas."
        ),
        instruction=(
            "You are the Pokémon world and encounters specialist. "
            "Use the available tools to retrieve accurate location and encounter data and return clear, "
            "well-formatted answers. "
            "Always use tools for factual data instead of guessing from memory."
        ),
        tools=world_tools,
    )


world_agent = create_world_agent()
