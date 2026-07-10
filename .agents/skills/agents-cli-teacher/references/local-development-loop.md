# The local ADK development loop

Use this reference when the conversation is about building and validating a
local ADK project from scaffold through evaluation.

## Core flow

1. Scaffold a production-shaped project.
2. Install exact dependencies.
3. Add or enhance deployment targets when needed.
4. Build and test locally with the playground or `agents-cli run`.
5. Lint before deeper testing.
6. Generate and grade evaluations.
7. Iterate until the traces and scores are stable.

## Scaffolding

Start with the prototype path when you want the smallest standard ADK template:

```bash
agents-cli scaffold create ambient-expense-agent --prototype --yes
cd ambient-expense-agent
agents-cli install
```

Use `agents-cli install` after scaffolding and whenever dependencies change.

## Project shape

A scaffolded project typically includes:

* `app/` for agent code
* `tests/` for unit, integration, and evaluation tests
* `pyproject.toml` for dependencies
* `uv.lock` for pinned versions
* `Makefile` for common commands
* `README.md` and `.gitignore`

The main agent entry point lives in `app/agent.py`.

## Local testing

Use the playground for interactive checks:

```bash
agents-cli playground
```

Use `agents-cli run` for fast one-off smoke tests.

Run linting before debugging behavior:

```bash
agents-cli lint
```

## Evaluation

Evaluation is the quality gate. The lesson frames it as an evaluation loop
with:

* a dataset file under `tests/eval/datasets/`
* a metric configuration file under `tests/eval/eval_config.yaml`

Run evaluation in two steps:

```bash
agents-cli eval generate
agents-cli eval grade
```

Regenerate traces after code changes before grading again.

## Deployment readiness

When you are ready to move beyond local testing, add a deployment target with
the enhance command instead of re-scaffolding.

Example:

```bash
agents-cli scaffold enhance --deployment-target cloud_run
```

## Prompting Antigravity

In the coding-agent flow, describe the intent rather than manually running the
commands yourself. For example, ask it to create the project, install
dependencies, and walk through the generated structure.

## What to watch for

* Keep `app/agent.py` as the module-level entry point.
* Commit `uv.lock` so environments stay reproducible.
* Re-run install when dependencies change.
* Prefer the prototype scaffold for the course's example structure.
