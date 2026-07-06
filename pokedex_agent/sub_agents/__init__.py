"""Sub-agents package — exports all specialized sub-agents."""

from pokedex_agent.factory import (
    create_ability_agent,
    create_all_sub_agents,
    create_item_agent,
    create_meta_agent,
    create_move_agent,
    create_pokemon_agent,
    create_world_agent,
)
from .pokemon import pokemon_agent
from .moves import move_agent
from .abilities import ability_agent
from .items import item_agent
from .world import world_agent
from .meta import meta_agent

all_sub_agents = [
    pokemon_agent,
    move_agent,
    ability_agent,
    item_agent,
    world_agent,
    meta_agent,
]

__all__ = [
    "pokemon_agent",
    "move_agent",
    "ability_agent",
    "item_agent",
    "world_agent",
    "meta_agent",
    "create_pokemon_agent",
    "create_move_agent",
    "create_ability_agent",
    "create_item_agent",
    "create_world_agent",
    "create_meta_agent",
    "create_all_sub_agents",
    "all_sub_agents",
]
