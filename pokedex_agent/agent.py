from google.adk.agents.llm_agent import Agent
import pokebase as pb

def get_pokemon(pokemon_name: str) -> str:
    """Get information about a Pokémon.

    Args:
        pokemon_name: The Pokémon name in English, like pikachu or charizard.
    """
    pokemon = pb.pokemon(pokemon_name)
    return str(pokemon)

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='An assistant that answers questions about Pokémon.',
    instruction='You are a Pokémon assistant. Answer questions about Pokémon, types, abilities, evolutions, and basic game information. Be clear and concise.',
    tools=[get_pokemon]
)
