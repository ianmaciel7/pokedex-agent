# google-agents-cli-eval Reference

Use this reference when adding, running, or interpreting evals for the Pokédex
ADK agent.

## Command Discovery

Do not assume the exact eval command. Start by discovering available commands:

```sh
google-agents-cli-eval --help
uv run google-agents-cli-eval --help
uv run adk eval --help
```

If none are available, report that the eval CLI is missing and ask whether to
add or install the package that provides it.

## Eval Inputs

Resolve these before creating or running evals:

- Agent or sub-agent entry point.
- Prompt language, especially English or Brazilian Portuguese.
- Expected routing behavior.
- Expected tool usage.
- Expected response traits, not brittle full-text matches unless necessary.
- Required credentials, without printing secret values.

## Suggested Coverage

Include small, focused cases for:

- English Pokémon lookup.
- Brazilian Portuguese request routing.
- Refusal to guess when data should come from tools.
- Tool-backed move, ability, item, world, or metadata lookups.
- Provider/model configuration behavior when relevant.

## Running Evals

Use the CLI's help output to choose the exact subcommand. Intended command shapes
may look like:

```sh
google-agents-cli-eval run --app pokedex_agent --evals EVAL_PATH
```

```sh
uv run adk eval pokedex_agent EVAL_PATH
```

If the installed CLI uses different nouns, map the workflow to the discovered
commands and report the command family used.

## Reporting

Report:

- Eval command used.
- Pass, fail, and skipped counts.
- Failing case names or prompts.
- Whether failures are behavior regressions, fixture issues, or environment
  issues.
- Any follow-up checks that could not run because credentials or commands were
  unavailable.

## Failure Handling

- Missing eval CLI: ask whether to add or install the package.
- Authentication failure: verify active credentials without printing secrets.
- Network/API failure: distinguish transient provider errors from agent logic
  failures.
- Ambiguous expected output: tighten the eval case before treating it as a
  product bug.
