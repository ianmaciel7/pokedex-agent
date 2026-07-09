"""Tools for items and berries."""

import pokebase as pb
from typing import NotRequired, TypedDict


class GetItemImageUrlInput(TypedDict):
    item_name: str


class GetItemImageUrlOutput(TypedDict):
    url: str | None


class GetItemImageUrlResponse(TypedDict):
    input: GetItemImageUrlInput
    output: GetItemImageUrlOutput
    error: NotRequired[str]


class GetItemInput(TypedDict):
    item_name: str


class GetItemOutput(TypedDict):
    value: str


class GetItemResponse(TypedDict):
    input: GetItemInput
    output: NotRequired[GetItemOutput]
    error: NotRequired[str]


class GetItemAttributeInput(TypedDict):
    item_attribute_name: str


class GetItemAttributeOutput(TypedDict):
    value: str


class GetItemAttributeResponse(TypedDict):
    input: GetItemAttributeInput
    output: NotRequired[GetItemAttributeOutput]
    error: NotRequired[str]


class GetItemCategoryInput(TypedDict):
    item_category_name: str


class GetItemCategoryOutput(TypedDict):
    value: str


class GetItemCategoryResponse(TypedDict):
    input: GetItemCategoryInput
    output: NotRequired[GetItemCategoryOutput]
    error: NotRequired[str]


class GetItemFlingEffectInput(TypedDict):
    item_fling_effect_name: str


class GetItemFlingEffectOutput(TypedDict):
    value: str


class GetItemFlingEffectResponse(TypedDict):
    input: GetItemFlingEffectInput
    output: NotRequired[GetItemFlingEffectOutput]
    error: NotRequired[str]


class GetItemPocketInput(TypedDict):
    item_pocket_name: str


class GetItemPocketOutput(TypedDict):
    value: str


class GetItemPocketResponse(TypedDict):
    input: GetItemPocketInput
    output: NotRequired[GetItemPocketOutput]
    error: NotRequired[str]


class GetBerryInput(TypedDict):
    berry_name: str


class GetBerryOutput(TypedDict):
    value: str


class GetBerryResponse(TypedDict):
    input: GetBerryInput
    output: NotRequired[GetBerryOutput]
    error: NotRequired[str]


class GetBerryFirmnessInput(TypedDict):
    berry_firmness_name: str


class GetBerryFirmnessOutput(TypedDict):
    value: str


class GetBerryFirmnessResponse(TypedDict):
    input: GetBerryFirmnessInput
    output: NotRequired[GetBerryFirmnessOutput]
    error: NotRequired[str]


class GetBerryFlavorInput(TypedDict):
    berry_flavor_name: str


class GetBerryFlavorOutput(TypedDict):
    value: str


class GetBerryFlavorResponse(TypedDict):
    input: GetBerryFlavorInput
    output: NotRequired[GetBerryFlavorOutput]
    error: NotRequired[str]


def get_item_image_url(item_name: str) -> GetItemImageUrlResponse:
    """Get the item sprite image URL for an item or berry.

    Args:
        item_name: The item name or berry name (e.g. 'potion', 'poke-ball', or 'cheri').
    """
    item = pb.item(item_name)
    url = item.sprites.default
    response: GetItemImageUrlResponse = {"input": {"item_name": item_name}, "output": {"url": url}}
    if url is None:
        response["error"] = "No sprite found for item."
    return response


def get_item(item_name: str) -> GetItemResponse:
    """Get information about an in-game item (effect, cost, held effects).

    Args:
        item_name: The item name or its ID (e.g. 'potion' or '17').
    """
    return {
        "input": {"item_name": item_name},
        "output": {"value": str(pb.item(item_name))},
    }


def get_item_attribute(item_attribute_name: str) -> GetItemAttributeResponse:
    """Get an item attribute (e.g. 'holdable', 'consumable').

    Args:
        item_attribute_name: The attribute name or its ID.
    """
    return {
        "input": {"item_attribute_name": item_attribute_name},
        "output": {"value": str(pb.item_attribute(item_attribute_name))},
    }


def get_item_category(item_category_name: str) -> GetItemCategoryResponse:
    """Get an item category (e.g. 'medicine', 'pokeballs').

    Args:
        item_category_name: The category name or its ID.
    """
    return {
        "input": {"item_category_name": item_category_name},
        "output": {"value": str(pb.item_category(item_category_name))},
    }


def get_item_fling_effect(item_fling_effect_name: str) -> GetItemFlingEffectResponse:
    """Get the effect of using Fling with a specific item.

    Args:
        item_fling_effect_name: The fling effect name or its ID.
    """
    return {
        "input": {"item_fling_effect_name": item_fling_effect_name},
        "output": {"value": str(pb.item_fling_effect(item_fling_effect_name))},
    }


def get_item_pocket(item_pocket_name: str) -> GetItemPocketResponse:
    """Get items grouped by the bag pocket they belong to (e.g. 'medicine', 'berries').

    Args:
        item_pocket_name: The pocket name or its ID.
    """
    return {
        "input": {"item_pocket_name": item_pocket_name},
        "output": {"value": str(pb.item_pocket(item_pocket_name))},
    }


def get_berry(berry_name: str) -> GetBerryResponse:
    """Get information about a berry (growth time, flavors, natural gift power/type).

    Args:
        berry_name: The berry name or its ID (e.g. 'cheri' or '1').
    """
    return {
        "input": {"berry_name": berry_name},
        "output": {"value": str(pb.berry(berry_name))},
    }


def get_berry_firmness(berry_firmness_name: str) -> GetBerryFirmnessResponse:
    """Get a berry firmness category (e.g. 'soft', 'hard').

    Args:
        berry_firmness_name: The firmness name or its ID.
    """
    return {
        "input": {"berry_firmness_name": berry_firmness_name},
        "output": {"value": str(pb.berry_firmness(berry_firmness_name))},
    }


def get_berry_flavor(berry_flavor_name: str) -> GetBerryFlavorResponse:
    """Get a berry flavor and the Pokémon natures that like/dislike it (e.g. 'spicy', 'sweet').

    Args:
        berry_flavor_name: The flavor name or its ID.
    """
    return {
        "input": {"berry_flavor_name": berry_flavor_name},
        "output": {"value": str(pb.berry_flavor(berry_flavor_name))},
    }


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
