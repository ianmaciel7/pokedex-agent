"""Sub-agent for Pokémon abilities and types."""

from google.adk.agents.llm_agent import Agent

from pokedex_agent.factory import create_sub_agent
from pokedex_agent.tools.abilities import ability_tools


def create_ability_agent() -> Agent:
    return create_sub_agent("ability", ability_tools)


ability_agent = create_ability_agent()
