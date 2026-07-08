"""Tools for game metadata: versions, contests, languages, and evolution."""

import pokebase as pb


def get_version(version_name: str) -> str:
    """Get information about a specific game version (e.g. 'red', 'gold', 'sword').

    Args:
        version_name: The game version name or its ID.
    """
    return str(pb.version(version_name))


def get_version_group(version_group_name: str) -> str:
    """Get a version group (paired games sharing mechanics, e.g. 'red-blue', 'sun-moon').

    Args:
        version_group_name: The version group name or its ID.
    """
    return str(pb.version_group(version_group_name))


def get_evolution_chain(evolution_chain_id: str) -> str:
    """Get the full evolution chain for a Pokémon family by chain ID.

    Args:
        evolution_chain_id: The numeric ID of the evolution chain.
    """
    return str(pb.evolution_chain(evolution_chain_id))


def get_evolution_trigger(evolution_trigger_name: str) -> str:
    """Get an evolution trigger (the condition that triggers evolution, e.g. 'level-up', 'trade').

    Args:
        evolution_trigger_name: The evolution trigger name or its ID.
    """
    return str(pb.evolution_trigger(evolution_trigger_name))


def get_contest_type(contest_type_name: str) -> str:
    """Get a Pokémon Contest type (e.g. 'cool', 'cute', 'smart').

    Args:
        contest_type_name: The contest type name or its ID.
    """
    return str(pb.contest_type(contest_type_name))


def get_contest_effect(contest_effect_id: str) -> str:
    """Get the effect of a move when used in a Pokémon Contest.

    Args:
        contest_effect_id: The numeric ID of the contest effect.
    """
    return str(pb.contest_effect(contest_effect_id))


def get_super_contest_effect(super_contest_effect_id: str) -> str:
    """Get the effect of a move when used in a Super Contest.

    Args:
        super_contest_effect_id: The numeric ID of the super contest effect.
    """
    return str(pb.super_contest_effect(super_contest_effect_id))


def get_language(language_name: str) -> str:
    """Get information about a supported game language (e.g. 'en', 'ja', 'fr').

    Args:
        language_name: The language name or its ID.
    """
    return str(pb.language(language_name))


meta_tools = [
    get_version,
    get_version_group,
    get_evolution_chain,
    get_evolution_trigger,
    get_contest_type,
    get_contest_effect,
    get_super_contest_effect,
    get_language,
]
