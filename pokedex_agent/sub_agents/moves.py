"""Sub-agent for Pokémon moves and battle mechanics."""

from google.adk.agents.llm_agent import Agent

from pokedex_agent.factory import create_sub_agent
from pokedex_agent.tools.moves import move_tools


def create_move_agent() -> Agent:
    return create_sub_agent(
        name="move_agent",
        description=(
            "Handles Pokémon move and battle-mechanics queries: move stats (power, accuracy, PP, type), "
            "machines, move ailments, damage classes, learn methods, move targets, move categories, "
            "and battle styles."
        ),
        instruction=(
            "You are the Pokémon move and battle-mechanics specialist. "
            "Use the available tools to retrieve accurate move data and return clear, "
            "well-formatted answers. "
            "Always use tools for factual data instead of guessing from memory."
        ),
        tools=move_tools,
    )


move_agent = create_move_agent()
