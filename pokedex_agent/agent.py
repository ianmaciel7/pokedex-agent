"""Root orchestrator agents for the Pokédex agent package."""

from google.adk.apps.app import App

from pokedex_agent.factory import create_root_agent
from pokedex_agent.plugins import GlobalErrorPlugin
from pokedex_agent.sub_agents import create_all_sub_agents


english_agent = create_root_agent("english", create_all_sub_agents())

pt_br_agent = create_root_agent("pt_br", create_all_sub_agents())

# ADK Web uses root_agent as the default entry point for this package.
root_agent = english_agent

app = App(
    name="pokedex_agent",
    root_agent=root_agent,
    plugins=[GlobalErrorPlugin()],
)

__all__ = ["app", "english_agent", "pt_br_agent", "root_agent"]
