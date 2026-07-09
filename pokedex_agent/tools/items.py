"""Tools for items and berries."""

import pokebase as pb
from pokedex_agent.tools.utils import safe_fetch


@safe_fetch
def get_item_image_url(item_name: str) -> str:
    """Get the item sprite image URL for an item or berry.

    Args:
        item_name: The item name or berry name (e.g. 'potion', 'poke-ball', or 'cheri').
    """
    item = pb.item(item_name)
    url = item.sprites.default
    if not url:
        return f"No sprite found for item {item_name}."
    return url


@safe_fetch
def get_item(item_name: str) -> str:
    """Get information about an in-game item (effect, cost, held effects).

    Args:
        item_name: The item name or its ID (e.g. 'potion' or '17').
    """
    return str(pb.item(item_name))


@safe_fetch
def get_item_attribute(item_attribute_name: str) -> str:
    """Get an item attribute (e.g. 'holdable', 'consumable').

    Args:
        item_attribute_name: The attribute name or its ID.
    """
    return str(pb.item_attribute(item_attribute_name))


@safe_fetch
def get_item_category(item_category_name: str) -> str:
    """Get an item category (e.g. 'medicine', 'pokeballs').

    Args:
        item_category_name: The category name or its ID.
    """
    return str(pb.item_category(item_category_name))


@safe_fetch
def get_item_fling_effect(item_fling_effect_name: str) -> str:
    """Get the effect of using Fling with a specific item.

    Args:
        item_fling_effect_name: The fling effect name or its ID.
    """
    return str(pb.item_fling_effect(item_fling_effect_name))


@safe_fetch
def get_item_pocket(item_pocket_name: str) -> str:
    """Get items grouped by the bag pocket they belong to (e.g. 'medicine', 'berries').

    Args:
        item_pocket_name: The pocket name or its ID.
    """
    return str(pb.item_pocket(item_pocket_name))


@safe_fetch
def get_berry(berry_name: str) -> str:
    """Get information about a berry (growth time, flavors, natural gift power/type).

    Args:
        berry_name: The berry name or its ID (e.g. 'cheri' or '1').
    """
    return str(pb.berry(berry_name))


@safe_fetch
def get_berry_firmness(berry_firmness_name: str) -> str:
    """Get a berry firmness category (e.g. 'soft', 'hard').

    Args:
        berry_firmness_name: The firmness name or its ID.
    """
    return str(pb.berry_firmness(berry_firmness_name))


@safe_fetch
def get_berry_flavor(berry_flavor_name: str) -> str:
    """Get a berry flavor and the Pokémon natures that like/dislike it (e.g. 'spicy', 'sweet').

    Args:
        berry_flavor_name: The flavor name or its ID.
    """
    return str(pb.berry_flavor(berry_flavor_name))


item_tools = [
    get_item_image_url,
    get_item,
    get_item_attribute,
    get_item_category,
    get_item_fling_effect,
    get_item_pocket,
    get_berry,
    get_berry_firmness,
    get_berry_flavor,
]
