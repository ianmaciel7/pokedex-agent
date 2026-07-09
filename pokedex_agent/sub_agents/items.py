"""Sub-agent for items and berries."""

from google.adk.agents.llm_agent import Agent

from pokedex_agent.factory import create_sub_agent
from pokedex_agent.tools.items import item_tools


def create_item_agent() -> Agent:
    return create_sub_agent("item", item_tools)


item_agent = create_item_agent()
