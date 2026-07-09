"""Sub-agent for items and berries."""

from google.adk.agents.llm_agent import Agent

from pokedex_agent.factory import create_sub_agent
from pokedex_agent.tools.items import item_tools


def create_item_agent() -> Agent:
    return create_sub_agent(
        name="item_agent",
        description=(
            "Handles item and berry queries: item descriptions and effects, item categories and bag pockets, "
            "Fling effects, item attributes, berry growth data, berry flavors and nature preferences, "
            "and berry firmness categories."
        ),
        instruction=(
            "You are the Pokémon items-and-berries specialist. "
            "Use the available tools to retrieve accurate item and berry data and return clear, "
            "well-formatted answers. "
            "Always use tools for factual data instead of guessing from memory."
        ),
        tools=item_tools,
    )


item_agent = create_item_agent()
