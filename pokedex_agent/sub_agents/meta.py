"""Sub-agent for game metadata: versions, contests, languages, and evolution."""

from google.adk.agents.llm_agent import Agent

from pokedex_agent.factory import create_sub_agent
from pokedex_agent.tools.meta import meta_tools


def create_meta_agent() -> Agent:
    return create_sub_agent("meta", meta_tools)


meta_agent = create_meta_agent()
