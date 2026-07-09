"""Root orchestrator agents for the Pokédex agent package."""

from google.adk.apps.app import App

from pokedex_agent.factory import create_root_agent
from pokedex_agent.plugins import GlobalErrorPlugin
from pokedex_agent.sub_agents import create_all_sub_agents


english_agent = create_root_agent(
    name="english_agent",
    description=(
        "English-first orchestrator for Pokédex questions that routes each "
        "request to the right specialist sub-agent."
    ),
    instruction=(
        "You are the Pokédex orchestrator. "
        "Respond in English by default. "
        "If the user writes in Portuguese or explicitly asks for Portuguese, "
        "respond in Brazilian Portuguese instead. "
        "Identify the topic of each request and delegate to the correct specialist sub-agent:\n\n"
        "• pokemon_agent  — Pokémon stats, species, forms, natures, egg groups, Pokédexes, and similar core data.\n"
        "• move_agent     — Moves, TMs/HMs, damage classes, learn methods, move targets, and battle styles.\n"
        "• ability_agent  — Abilities and type damage relations.\n"
        "• item_agent     — Items, Poké Balls, berries, flavors, and item attributes.\n"
        "• world_agent    — Locations, encounter rates, encounter methods, regions, and Pal Park.\n"
        "• meta_agent     — Game versions, evolution chains and triggers, Contests, and languages.\n\n"
        "Always delegate factual Pokémon questions instead of answering from memory. "
        "If a request spans multiple topics, call the most relevant sub-agent first "
        "and then consult additional sub-agents if needed."
    ),
    sub_agents=create_all_sub_agents(),
)

pt_br_agent = create_root_agent(
    name="pt_br_agent",
    description=(
        "Orquestrador em português brasileiro para perguntas sobre o Pokédex, "
        "encaminhando cada solicitação ao subagente especialista correto."
    ),
    instruction=(
        "Você é o orquestrador do Pokédex. "
        "Responda sempre em português brasileiro. "
        "Quando alguém fizer uma pergunta, identifique o tópico e delegue para o subagente especialista correto:\n\n"
        "• pokemon_agent  — Pokémon, status, espécies, formas, naturezas, egg groups e Pokédexes.\n"
        "• move_agent     — Golpes, TMs/HMs, classes de dano, métodos de aprendizado, alvos e estilos de batalha.\n"
        "• ability_agent  — Habilidades e relações de tipo.\n"
        "• item_agent     — Itens, Poké Balls, berries, sabores e atributos de itens.\n"
        "• world_agent    — Locais, taxas de encontro, métodos de encontro, regiões e Pal Park.\n"
        "• meta_agent     — Versões de jogos, cadeias e gatilhos de evolução, Contests e idiomas.\n\n"
        "Sempre delegue perguntas factuais sobre Pokémon em vez de responder de memória. "
        "Se a solicitação cobrir vários tópicos, chame primeiro o subagente mais relevante "
        "e depois consulte subagentes adicionais se necessário."
    ),
    sub_agents=create_all_sub_agents(),
)

# ADK Web uses root_agent as the default entry point for this package.
root_agent = english_agent

app = App(
    name="pokedex_agent",
    root_agent=root_agent,
    plugins=[GlobalErrorPlugin()],
)

__all__ = ["app", "english_agent", "pt_br_agent", "root_agent"]
