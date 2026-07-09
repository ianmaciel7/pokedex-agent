"""Sub-agent for Pokémon abilities and types."""

from google.adk.agents.llm_agent import Agent

from pokedex_agent.factory import create_sub_agent
from pokedex_agent.tools.abilities import ability_tools


def create_ability_agent() -> Agent:
    return create_sub_agent(
        name="ability_agent",
        description=(
            "Handles Pokémon ability and type queries: ability descriptions and effects, "
            "which Pokémon have a given ability, type damage relations, and Pokémon belonging to a type."
        ),
        instruction=(
            "You are the Pokémon abilities-and-types specialist. "
            "Use the available tools to retrieve accurate ability and type data and return clear, "
            "well-formatted answers. "
            "Always use tools for factual data instead of guessing from memory."
        ),
        tools=ability_tools,
    )


ability_agent = create_ability_agent()
