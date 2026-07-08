"""Sub-agent for Pokémon moves and battle mechanics."""

from google.adk.agents.llm_agent import Agent

from pokedex_agent.factory import create_sub_agent
from pokedex_agent.tools.moves import move_tools


def create_move_agent() -> Agent:
    return create_sub_agent(
        name="move_agent",
        description=(
            "Handles queries about Pokémon moves and battle mechanics: move stats (power, accuracy, PP, type), "
            "TMs and HMs (machines), move ailments (status conditions), damage classes (physical/special/status), "
            "learn methods (level-up, egg, tutor), move targets, move categories, and battle styles."
        ),
        instruction=(
            "You are a Pokémon move and battle mechanics specialist. "
            "Use the available tools to look up accurate data about moves and return clear, "
            "well-formatted answers. "
            "Always use the tool — never guess move data from memory."
        ),
        tools=move_tools,
    )


move_agent = create_move_agent()
