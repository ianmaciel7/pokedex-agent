"""Sub-agent for items and berries."""

from google.adk.agents.llm_agent import Agent
from pokedex_agent.tools.items import item_tools

item_agent = Agent(
    model="gemini-2.0-flash",
    name="item_agent",
    description=(
        "Handles queries about items and berries: item descriptions and effects, item categories "
        "and bag pockets, Fling effects, item attributes (holdable, consumable, etc.), "
        "berry growth data, berry flavors and nature preferences, and berry firmness categories."
    ),
    instruction=(
        "You are a Pokémon items and berries specialist. "
        "Use the available tools to look up accurate data about items and berries, "
        "and return clear, well-formatted answers. "
        "Always use the tool — never guess item or berry data from memory."
    ),
    tools=item_tools,
)
