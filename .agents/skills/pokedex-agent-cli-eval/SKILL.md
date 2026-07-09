---
name: pokedex-agent-cli-eval
description: Design, add, run, or interpret evaluations for the local pokedex-agent Google ADK package with Google Agents CLI or ADK eval tooling. Use when Codex is asked for Pokédex agent evals, evaluation datasets, regression checks, quality scoring, or behavior validation.
---

# Pokédex Agent CLI Eval

## Original Skill Reference

This is the Pokédex-local adaptation of the original `google-agents-cli-eval`
skill. Keep the generic CLI guidance in `references/google-agents-cli-eval.md`
as the source reference, then apply the repository-specific rules in this file.

## Overview

Use this skill to add or run focused evaluations for ADK agent behavior.
Drive evaluation lifecycle work through `google-agents-cli-eval` or ADK eval
commands when they are installed. If the CLI surface differs, discover it with
`--help` and adapt the workflow to the available commands.

Treat evals as regression checks for agent behavior, routing, tool use, and
language handling. Keep eval artifacts free of secrets and local environment
values.

## Workflow

1. Confirm the repository looks like this package:
   - `pyproject.toml` project name is `pokedex-agent`.
   - `pokedex_agent/agent.py` exports the ADK entry point.
   - `pokedex_agent` imports locally without syntax errors.
2. Identify the behavior under test, including the agent entry point, expected
   output traits, tool use, and routing behavior.
3. Discover the installed eval command before using it:
   - Try `google-agents-cli-eval --help`.
   - If that fails, try `uv run google-agents-cli-eval --help`.
   - If neither exists, try `uv run adk eval --help`.
4. Prefer small regression cases with clear expectations over broad prompts.
5. Include multilingual cases when behavior touches English or Brazilian
   Portuguese routing.
6. Parse and report pass/fail counts, skipped checks, and notable failures.

## Safety Rules

- Do not include API keys, tokens, credentials, or local `.env` values in eval
  fixtures, command output, or logs.
- Treat eval prompts and expected outputs as test assets; avoid unrelated
  rewrites.
- For factual Pokémon data, expect the agent to use tools instead of memory.
- Do not mark an eval pass if command output is ambiguous or incomplete.

## Pokédex Preflight

Run this check before finishing code-backed eval work:

```sh
uv run ruff check pokedex_agent
```

After changing imports, exports, factories, or agent wiring for an eval, also
run:

```sh
uv run python -c "import pokedex_agent.agent; from pokedex_agent.sub_agents import create_all_sub_agents; print(len(create_all_sub_agents()))"
```

## CLI Guidance

Read `references/google-agents-cli-eval.md` when planning, adding, running, or
interpreting evals. Use the reference as a pattern, then prefer the installed
CLI's `--help` output over any remembered syntax.
