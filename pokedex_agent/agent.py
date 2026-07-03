from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='An assistant that answers questions about Pokémon.',
    instruction='You are a Pokémon assistant. Answer questions about Pokémon, types, abilities, evolutions, and basic game information. Be clear and concise.',
)
