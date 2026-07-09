"""Sub-agent for Pokémon moves and battle mechanics."""

from google.adk.agents.llm_agent import Agent

from pokedex_agent.factory import create_sub_agent
from pokedex_agent.tools.moves import move_tools


def create_move_agent() -> Agent:
    return create_sub_agent("move", move_tools)


move_agent = create_move_agent()
