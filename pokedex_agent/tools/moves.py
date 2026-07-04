"""Tools for Pokémon moves and battle mechanics."""

import pokebase as pb


def get_move(move_name: str) -> str:
    """Get detailed information about a Pokémon move (power, accuracy, type, PP).

    Args:
        move_name: The move name or its ID (e.g. 'flamethrower' or '53').
    """
    return str(pb.move(move_name))


def get_move_ailment(move_ailment_name: str) -> str:
    """Get a move ailment (status condition a move can inflict, e.g. 'burn', 'paralysis').

    Args:
        move_ailment_name: The ailment name or its ID.
    """
    return str(pb.move_ailment(move_ailment_name))


def get_move_battle_style(move_battle_style_name: str) -> str:
    """Get a move battle style used in Pokémon Battle Palace (e.g. 'attack', 'defense').

    Args:
        move_battle_style_name: The battle style name or its ID.
    """
    return str(pb.move_battle_style(move_battle_style_name))


def get_move_category(move_category_name: str) -> str:
    """Get a move category (e.g. 'damage', 'ailment', 'heal').

    Args:
        move_category_name: The category name or its ID.
    """
    return str(pb.move_category(move_category_name))


def get_move_damage_class(move_damage_class_name: str) -> str:
    """Get a move damage class (e.g. 'physical', 'special', 'status').

    Args:
        move_damage_class_name: The damage class name or its ID.
    """
    return str(pb.move_damage_class(move_damage_class_name))


def get_move_learn_method(move_learn_method_name: str) -> str:
    """Get a method by which a Pokémon can learn a move (e.g. 'level-up', 'egg', 'tutor').

    Args:
        move_learn_method_name: The learn method name or its ID.
    """
    return str(pb.move_learn_method(move_learn_method_name))


def get_move_target(move_target_name: str) -> str:
    """Get a move target (who the move affects, e.g. 'selected-pokemon', 'all-opponents').

    Args:
        move_target_name: The target name or its ID.
    """
    return str(pb.move_target(move_target_name))


def get_machine(machine_id: str) -> str:
    """Get information about a TM or HM machine (which move it teaches, which games it appears in).

    Args:
        machine_id: The numeric ID of the machine.
    """
    return str(pb.machine(machine_id))


move_tools = [
    get_move,
    get_move_ailment,
    get_move_battle_style,
    get_move_category,
    get_move_damage_class,
    get_move_learn_method,
    get_move_target,
    get_machine,
]
