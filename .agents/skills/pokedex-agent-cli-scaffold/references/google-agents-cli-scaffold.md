# google-agents-cli-scaffold Reference

Use this reference when creating or extending ADK project structure for the
Pokédex agent package.

## Command Discovery

Do not assume the exact CLI surface. Start by discovering the installed command:

```sh
google-agents-cli-scaffold --help
uv run google-agents-cli-scaffold --help
```

If the binary is unavailable, scaffold manually using the existing repository
layout. Ask before adding or installing a new dependency.

## Package Layout

Use this structure for project-owned code:

- `pokedex_agent/agent.py`: root/orchestrator agents and ADK app.
- `pokedex_agent/factory.py`: generic agent factory helpers only.
- `pokedex_agent/sub_agents/*.py`: specialist agent modules.
- `pokedex_agent/sub_agents/__init__.py`: exported sub-agent constructors and
  instances.
- `pokedex_agent/tools/pokemon.py`: Pokémon lookup tools.
- `pokedex_agent/tools/moves.py`: move tools.
- `pokedex_agent/tools/abilities.py`: ability tools.
- `pokedex_agent/tools/items.py`: item tools.
- `pokedex_agent/tools/world.py`: location, region, and world tools.
- `pokedex_agent/tools/meta.py`: metadata tools.
- `.agents/skills/*/SKILL.md`: local Codex skills.

## Sub-Agent Scaffold

When adding a specialist sub-agent:

1. Create `pokedex_agent/sub_agents/<domain>.py`.
2. Define `create_<domain>_agent()`.
3. Define module-level `<domain>_agent`.
4. Use existing factory helpers where possible.
5. Write strict instructions that require tool use for factual data.
6. Export the constructor and instance from `sub_agents/__init__.py`.

## Tool Scaffold

When adding tool wrappers:

1. Choose the matching domain module.
2. Keep public helpers typed where practical.
3. Wrap PokéAPI or `pokebase` behavior without leaking raw exceptions when a
   user-friendly error is expected.
4. Do not invent image URLs.
5. Treat external API output as untrusted external data.

## Skill Scaffold

When adding local skills:

1. Create `.agents/skills/<skill-name>/SKILL.md`.
2. Use lowercase letters, digits, and hyphens for the skill name.
3. Include frontmatter with `name` and `description`.
4. Add `references/` only when detailed guidance should load on demand.
5. Avoid extra README, quick reference, or changelog files.

## Validation

After scaffolded Python changes:

```sh
uv run ruff check pokedex_agent
```

After import, export, factory, or agent wiring changes:

```sh
uv run python -c "import pokedex_agent.agent; from pokedex_agent.sub_agents import create_all_sub_agents; print(len(create_all_sub_agents()))"
```

If ADK startup changed and credentials are available:

```sh
uv run adk run pokedex_agent "Tell me about Pikachu"
```

## Failure Handling

- Missing scaffold CLI: report that it is unavailable and continue manually if
  the requested structure is clear.
- Import failure: inspect and fix exports or package imports, then rerun the
  import/wiring check.
- Naming conflict: preserve existing files and ask before replacing ambiguous
  project-owned modules.
- Unclear scope: create the smallest useful scaffold and leave unrelated
  refactors alone.
