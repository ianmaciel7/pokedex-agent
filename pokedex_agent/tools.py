import pokebase as pb

# This file contains wrapper tools for all endpoints in the pokebase package.
# They return a string representation of the retrieved resource data.

def get_ability(ability_name: str) -> str:
    """Get information about a Pokémon ability.

    Args:
        ability_name: The name or ID of the Pokémon ability.
    """
    res = pb.ability(ability_name)
    return str(res)

def get_berry(berry_name: str) -> str:
    """Get information about a Berry.

    Args:
        berry_name: The name or ID of the berry.
    """
    res = pb.berry(berry_name)
    return str(res)

def get_berry_firmness(berry_firmness_name: str) -> str:
    """Get information about a Berry firmness type.

    Args:
        berry_firmness_name: The name or ID of the berry firmness type.
    """
    res = pb.berry_firmness(berry_firmness_name)
    return str(res)

def get_berry_flavor(berry_flavor_name: str) -> str:
    """Get information about a Berry flavor.

    Args:
        berry_flavor_name: The name or ID of the berry flavor.
    """
    res = pb.berry_flavor(berry_flavor_name)
    return str(res)

def get_characteristic(characteristic_id: str) -> str:
    """Get information about a Pokémon characteristic by ID.

    Args:
        characteristic_id: The name or ID of the Pokémon characteristic by ID.
    """
    res = pb.characteristic(characteristic_id)
    return str(res)

def get_contest_effect(contest_effect_id: str) -> str:
    """Get information about a Contest effect by ID.

    Args:
        contest_effect_id: The name or ID of the contest effect by ID.
    """
    res = pb.contest_effect(contest_effect_id)
    return str(res)

def get_contest_type(contest_type_name: str) -> str:
    """Get information about a Contest type.

    Args:
        contest_type_name: The name or ID of the contest type.
    """
    res = pb.contest_type(contest_type_name)
    return str(res)

def get_egg_group(egg_group_name: str) -> str:
    """Get information about a Pokémon egg group.

    Args:
        egg_group_name: The name or ID of the Pokémon egg group.
    """
    res = pb.egg_group(egg_group_name)
    return str(res)

def get_encounter_condition(encounter_condition_name: str) -> str:
    """Get information about a Encounter condition.

    Args:
        encounter_condition_name: The name or ID of the encounter condition.
    """
    res = pb.encounter_condition(encounter_condition_name)
    return str(res)

def get_encounter_condition_value(encounter_condition_value_name: str) -> str:
    """Get information about a Encounter condition value.

    Args:
        encounter_condition_value_name: The name or ID of the encounter condition value.
    """
    res = pb.encounter_condition_value(encounter_condition_value_name)
    return str(res)

def get_encounter_method(encounter_method_name: str) -> str:
    """Get information about a Encounter method.

    Args:
        encounter_method_name: The name or ID of the encounter method.
    """
    res = pb.encounter_method(encounter_method_name)
    return str(res)

def get_evolution_chain(evolution_chain_id: str) -> str:
    """Get information about a Evolution chain by ID.

    Args:
        evolution_chain_id: The name or ID of the evolution chain by ID.
    """
    res = pb.evolution_chain(evolution_chain_id)
    return str(res)

def get_evolution_trigger(evolution_trigger_name: str) -> str:
    """Get information about a Evolution trigger.

    Args:
        evolution_trigger_name: The name or ID of the evolution trigger.
    """
    res = pb.evolution_trigger(evolution_trigger_name)
    return str(res)

def get_gender(gender_name: str) -> str:
    """Get information about a Gender.

    Args:
        gender_name: The name or ID of the gender.
    """
    res = pb.gender(gender_name)
    return str(res)

def get_generation(generation_name: str) -> str:
    """Get information about a Pokémon generation.

    Args:
        generation_name: The name or ID of the Pokémon generation.
    """
    res = pb.generation(generation_name)
    return str(res)

def get_growth_rate(growth_rate_name: str) -> str:
    """Get information about a Pokémon growth rate.

    Args:
        growth_rate_name: The name or ID of the Pokémon growth rate.
    """
    res = pb.growth_rate(growth_rate_name)
    return str(res)

def get_item(item_name: str) -> str:
    """Get information about a Item.

    Args:
        item_name: The name or ID of the item.
    """
    res = pb.item(item_name)
    return str(res)

def get_item_attribute(item_attribute_name: str) -> str:
    """Get information about a Item attribute.

    Args:
        item_attribute_name: The name or ID of the item attribute.
    """
    res = pb.item_attribute(item_attribute_name)
    return str(res)

def get_item_category(item_category_name: str) -> str:
    """Get information about a Item category.

    Args:
        item_category_name: The name or ID of the item category.
    """
    res = pb.item_category(item_category_name)
    return str(res)

def get_item_fling_effect(item_fling_effect_name: str) -> str:
    """Get information about a Item fling effect.

    Args:
        item_fling_effect_name: The name or ID of the item fling effect.
    """
    res = pb.item_fling_effect(item_fling_effect_name)
    return str(res)

def get_item_pocket(item_pocket_name: str) -> str:
    """Get information about a Item pocket.

    Args:
        item_pocket_name: The name or ID of the item pocket.
    """
    res = pb.item_pocket(item_pocket_name)
    return str(res)

def get_language(language_name: str) -> str:
    """Get information about a Language.

    Args:
        language_name: The name or ID of the language.
    """
    res = pb.language(language_name)
    return str(res)

def get_location(location_name: str) -> str:
    """Get information about a Location.

    Args:
        location_name: The name or ID of the location.
    """
    res = pb.location(location_name)
    return str(res)

def get_location_area(location_area_name: str) -> str:
    """Get information about a Location area.

    Args:
        location_area_name: The name or ID of the location area.
    """
    res = pb.location_area(location_area_name)
    return str(res)

def get_machine(machine_id: str) -> str:
    """Get information about a Machine by ID.

    Args:
        machine_id: The name or ID of the machine by ID.
    """
    res = pb.machine(machine_id)
    return str(res)

def get_move(move_name: str) -> str:
    """Get information about a Pokémon move.

    Args:
        move_name: The name or ID of the Pokémon move.
    """
    res = pb.move(move_name)
    return str(res)

def get_move_ailment(move_ailment_name: str) -> str:
    """Get information about a Move ailment.

    Args:
        move_ailment_name: The name or ID of the move ailment.
    """
    res = pb.move_ailment(move_ailment_name)
    return str(res)

def get_move_battle_style(move_battle_style_name: str) -> str:
    """Get information about a Move battle style.

    Args:
        move_battle_style_name: The name or ID of the move battle style.
    """
    res = pb.move_battle_style(move_battle_style_name)
    return str(res)

def get_move_category(move_category_name: str) -> str:
    """Get information about a Move category.

    Args:
        move_category_name: The name or ID of the move category.
    """
    res = pb.move_category(move_category_name)
    return str(res)

def get_move_damage_class(move_damage_class_name: str) -> str:
    """Get information about a Move damage class.

    Args:
        move_damage_class_name: The name or ID of the move damage class.
    """
    res = pb.move_damage_class(move_damage_class_name)
    return str(res)

def get_move_learn_method(move_learn_method_name: str) -> str:
    """Get information about a Move learn method.

    Args:
        move_learn_method_name: The name or ID of the move learn method.
    """
    res = pb.move_learn_method(move_learn_method_name)
    return str(res)

def get_move_target(move_target_name: str) -> str:
    """Get information about a Move target.

    Args:
        move_target_name: The name or ID of the move target.
    """
    res = pb.move_target(move_target_name)
    return str(res)

def get_nature(nature_name: str) -> str:
    """Get information about a Pokémon nature.

    Args:
        nature_name: The name or ID of the Pokémon nature.
    """
    res = pb.nature(nature_name)
    return str(res)

def get_pal_park_area(pal_park_area_name: str) -> str:
    """Get information about a Pal Park area.

    Args:
        pal_park_area_name: The name or ID of the Pal Park area.
    """
    res = pb.pal_park_area(pal_park_area_name)
    return str(res)

def get_pokeathlon_stat(pokeathlon_stat_name: str) -> str:
    """Get information about a Pokeathlon stat.

    Args:
        pokeathlon_stat_name: The name or ID of the Pokeathlon stat.
    """
    res = pb.pokeathlon_stat(pokeathlon_stat_name)
    return str(res)

def get_pokedex(pokedex_name: str) -> str:
    """Get information about a Pokedex.

    Args:
        pokedex_name: The name or ID of the Pokedex.
    """
    res = pb.pokedex(pokedex_name)
    return str(res)

def get_pokemon(pokemon_name: str) -> str:
    """Get information about a Pokémon.

    Args:
        pokemon_name: The name or ID of the Pokémon.
    """
    res = pb.pokemon(pokemon_name)
    return str(res)

def get_pokemon_color(pokemon_color_name: str) -> str:
    """Get information about a Pokémon color.

    Args:
        pokemon_color_name: The name or ID of the Pokémon color.
    """
    res = pb.pokemon_color(pokemon_color_name)
    return str(res)

def get_pokemon_form(pokemon_form_name: str) -> str:
    """Get information about a Pokémon form.

    Args:
        pokemon_form_name: The name or ID of the Pokémon form.
    """
    res = pb.pokemon_form(pokemon_form_name)
    return str(res)

def get_pokemon_habitat(pokemon_habitat_name: str) -> str:
    """Get information about a Pokémon habitat.

    Args:
        pokemon_habitat_name: The name or ID of the Pokémon habitat.
    """
    res = pb.pokemon_habitat(pokemon_habitat_name)
    return str(res)

def get_pokemon_shape(pokemon_shape_name: str) -> str:
    """Get information about a Pokémon shape.

    Args:
        pokemon_shape_name: The name or ID of the Pokémon shape.
    """
    res = pb.pokemon_shape(pokemon_shape_name)
    return str(res)

def get_pokemon_species(pokemon_species_name: str) -> str:
    """Get information about a Pokémon species.

    Args:
        pokemon_species_name: The name or ID of the Pokémon species.
    """
    res = pb.pokemon_species(pokemon_species_name)
    return str(res)

def get_region(region_name: str) -> str:
    """Get information about a Region.

    Args:
        region_name: The name or ID of the region.
    """
    res = pb.region(region_name)
    return str(res)

def get_stat(stat_name: str) -> str:
    """Get information about a Stat.

    Args:
        stat_name: The name or ID of the stat.
    """
    res = pb.stat(stat_name)
    return str(res)

def get_super_contest_effect(super_contest_effect_id: str) -> str:
    """Get information about a Super contest effect by ID.

    Args:
        super_contest_effect_id: The name or ID of the super contest effect by ID.
    """
    res = pb.super_contest_effect(super_contest_effect_id)
    return str(res)

def get_type(type_name: str) -> str:
    """Get information about a Pokémon type.

    Args:
        type_name: The name or ID of the Pokémon type.
    """
    res = pb.type_(type_name)
    return str(res)

def get_version(version_name: str) -> str:
    """Get information about a Game version.

    Args:
        version_name: The name or ID of the game version.
    """
    res = pb.version(version_name)
    return str(res)

def get_version_group(version_group_name: str) -> str:
    """Get information about a Game version group.

    Args:
        version_group_name: The name or ID of the game version group.
    """
    res = pb.version_group(version_group_name)
    return str(res)

def describe_all_tools() -> str:
    """Return a nicely‑formatted summary of all available pokebase tools.

    Example output:
    ```
    get_ability(name) – Get information about a Pokémon ability.
    get_berry(name) – Get information about a Berry.
    …
    get_version_group(name) – Get information about a Game version group.
    ```
    """
    lines = []
    for fn in all_tools:
        doc = (fn.__doc__ or "").strip().splitlines()
        summary = doc[0] if doc else "No description"
        arg_name = fn.__code__.co_varnames[0] if fn.__code__.co_argcount else ""
        lines.append(f"{fn.__name__}({arg_name}) – {summary}")
    return "\n".join(lines)


all_tools = [
    get_ability,
    get_berry,
    get_berry_firmness,
    get_berry_flavor,
    get_characteristic,
    get_contest_effect,
    get_contest_type,
    get_egg_group,
    get_encounter_condition,
    get_encounter_condition_value,
    get_encounter_method,
    get_evolution_chain,
    get_evolution_trigger,
    get_gender,
    get_generation,
    get_growth_rate,
    get_item,
    get_item_attribute,
    get_item_category,
    get_item_fling_effect,
    get_item_pocket,
    get_language,
    get_location,
    get_location_area,
    get_machine,
    get_move,
    get_move_ailment,
    get_move_battle_style,
    get_move_category,
    get_move_damage_class,
    get_move_learn_method,
    get_move_target,
    get_nature,
    get_pal_park_area,
    get_pokeathlon_stat,
    get_pokedex,
    get_pokemon,
    get_pokemon_color,
    get_pokemon_form,
    get_pokemon_habitat,
    get_pokemon_shape,
    get_pokemon_species,
    get_region,
    get_stat,
    get_super_contest_effect,
    get_type,
    get_version,
    get_version_group,
    describe_all_tools,
]
