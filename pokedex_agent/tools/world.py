"""Tools for locations, encounters, and regions."""

import pokebase as pb


def get_location(location_name: str) -> str:
    """Get information about a location in the Pokémon world (e.g. 'pallet-town').

    Args:
        location_name: The location name or its ID.
    """
    return str(pb.location(location_name))


def get_location_area(location_area_name: str) -> str:
    """Get a specific area within a location and its wild Pokémon encounter rates.

    Args:
        location_area_name: The location area name or its ID.
    """
    return str(pb.location_area(location_area_name))


def get_region(region_name: str) -> str:
    """Get information about a game region (e.g. 'kanto', 'johto').

    Args:
        region_name: The region name or its ID.
    """
    return str(pb.region(region_name))


def get_encounter_condition(encounter_condition_name: str) -> str:
    """Get a condition that affects wild Pokémon encounters (e.g. 'swarm', 'time').

    Args:
        encounter_condition_name: The condition name or its ID.
    """
    return str(pb.encounter_condition(encounter_condition_name))


def get_encounter_condition_value(encounter_condition_value_name: str) -> str:
    """Get a specific value for an encounter condition (e.g. 'time-morning').

    Args:
        encounter_condition_value_name: The condition value name or its ID.
    """
    return str(pb.encounter_condition_value(encounter_condition_value_name))


def get_encounter_method(encounter_method_name: str) -> str:
    """Get a method of encountering wild Pokémon (e.g. 'walk', 'surf', 'fishing').

    Args:
        encounter_method_name: The encounter method name or its ID.
    """
    return str(pb.encounter_method(encounter_method_name))


def get_pal_park_area(pal_park_area_name: str) -> str:
    """Get a Pal Park area (e.g. 'field', 'forest', 'mountain', 'pond', 'sea').

    Args:
        pal_park_area_name: The Pal Park area name or its ID.
    """
    return str(pb.pal_park_area(pal_park_area_name))


world_tools = [
    get_location,
    get_location_area,
    get_region,
    get_encounter_condition,
    get_encounter_condition_value,
    get_encounter_method,
    get_pal_park_area,
]
