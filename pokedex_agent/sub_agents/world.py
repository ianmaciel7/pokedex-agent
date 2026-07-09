"""Sub-agent for locations, encounters, and regions."""

from google.adk.agents.llm_agent import Agent

from pokedex_agent.factory import create_sub_agent
from pokedex_agent.tools.world import world_tools


def create_world_agent() -> Agent:
    return create_sub_agent("world", world_tools)


world_agent = create_world_agent()
