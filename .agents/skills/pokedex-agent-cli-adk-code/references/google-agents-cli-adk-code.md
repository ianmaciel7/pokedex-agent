# google-agents-cli-adk-code Reference

Use this reference when editing or generating ADK Python code for the Pokédex
agent package.

## Command Discovery

Do not assume the exact CLI surface. Start by discovering available commands:

```sh
google-agents-cli-adk-code --help
uv run google-agents-cli-adk-code --help
uv run adk --help
uv run adk run --help
```

If the binary is unavailable, continue with repository conventions and ADK
imports already present in the project. Ask before adding new dependencies.

## Code Areas

- `pokedex_agent/agent.py`: root/orchestrator wiring and ADK app entry point.
- `pokedex_agent/factory.py`: generic agent factory helpers only.
- `pokedex_agent/sub_agents/*.py`: specialist agent constructors and instances.
- `pokedex_agent/sub_agents/__init__.py`: collected constructors and instances.
- `pokedex_agent/tools/`: tool wrappers grouped by domain.
- `pokedex_agent/model_config.py`: provider and model configuration.

## Agent Changes

For a new or changed specialist sub-agent:

1. Inspect nearby sub-agent modules first.
2. Define a `create_*_agent()` factory.
3. Define a module-level `*_agent` instance.
4. Keep instructions strict about using tools for factual Pokémon data.
5. Export the constructor and instance from `sub_agents/__init__.py`.
6. Run Ruff and the import/wiring check.

## Tool Changes

For a new or changed tool wrapper:

1. Place it in the matching domain module: `pokemon`, `moves`, `abilities`,
   `items`, `world`, or `meta`.
2. Treat PokéAPI and `pokebase` output as external data.
3. Do not invent image URLs; return only tool-provided URLs.
4. Keep public helpers typed where practical.
5. Add focused validation for imports and agent wiring when exports change.

## Runtime Checks

Run these after code changes:

```sh
uv run ruff check pokedex_agent
uv run python -c "import pokedex_agent.agent; from pokedex_agent.sub_agents import create_all_sub_agents; print(len(create_all_sub_agents()))"
```

If behavior changed and credentials are available, run:

```sh
uv run adk run pokedex_agent "Tell me about Pikachu"
```

## Failure Handling

- Import failure: inspect the traceback, fix the local import or export, and
  rerun the import/wiring check.
- Missing dependency: ask whether to add the dependency to the project.
- Authentication failure during ADK runtime: verify credentials without printing
  secret values.
- Ambiguous CLI syntax: summarize the relevant help output and use the command
  form documented by the installed CLI.
