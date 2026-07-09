# google-agents-cli-workflow Reference

Use this reference when planning or running an end-to-end Google ADK agent
development workflow for the Pokédex agent package.

## Original Skill

This reference preserves the generic `google-agents-cli-workflow` intent for
the repository-local `pokedex-agent-cli-workflow` skill. Treat this file as the
source reference for generic Google Agents CLI workflow behavior, then apply the
Pokédex-specific conventions from the parent `SKILL.md`.

## Command Discovery

Do not assume the exact CLI surface. Start by discovering available commands:

```sh
uv run adk --help
uv run adk run --help
uv run adk eval --help
google-agents-cli-deploy --help
uv run google-agents-cli-deploy --help
```

If a dedicated Google Agents CLI command is unavailable, continue with the
installed ADK command surface and repository conventions. Ask before adding new
dependencies.

## Workflow Phases

Use the narrow local skills as the workflow moves from planning into action:

- `pokedex-agent-cli-adk-code` for ADK Python code, tools, callbacks, model
  configuration, and sub-agent wiring.
- `pokedex-agent-cli-scaffold` for package structure, sub-agents, tool modules,
  and local skills.
- `pokedex-agent-cli-eval` for behavior evals and regression checks.
- `pokedex-agent-cli-observability` for deployed logs, traces, metrics, and
  runtime inspection.
- `pokedex-agent-cli-deploy` for Agent Runtime / Agent Engine deployment
  lifecycle actions.

## Local Quality Gates

Run these checks before cloud actions or when code changed:

```sh
uv run ruff check pokedex_agent
uv run python -c "import pokedex_agent.agent; from pokedex_agent.sub_agents import create_all_sub_agents; print(len(create_all_sub_agents()))"
```

For behavior checks, prefer focused ADK runs when credentials are available:

```sh
uv run adk run pokedex_agent "Tell me about Pikachu"
```

## Reporting

Report:

- The phase or skill used.
- The commands run.
- Whether checks passed, failed, or were skipped.
- Any credential, command availability, or cloud target assumptions.
- The next safest action if a phase cannot continue.

## Safety

- Do not print or commit API keys, tokens, credentials, or local `.env` values.
- Verify project, region, target, and deployment identity before cloud actions.
- Treat eval fixtures, logs, and traces as potentially sensitive.
- Prefer installed CLI help output over remembered syntax.
