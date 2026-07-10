# Local development loop

Use this reference when the conversation is about the standard local ADK
development loop, project shape, testing, evaluation, and deployment readiness.

## Core loop

1. Scaffold a production-shaped project.
2. Install exact dependencies.
3. Add or enhance deployment targets when needed.
4. Build and test locally with the playground or `agents-cli run`.
5. Lint before deeper testing.
6. Generate and grade evaluations.
7. Iterate until traces and scores are stable.

## Project shape and entry point

A scaffolded project typically includes:

* `app/` for agent code
* `tests/` for unit, integration, and evaluation tests
* `pyproject.toml` for dependencies
* `uv.lock` for pinned versions
* `Makefile` for common commands
* `README.md` and `.gitignore`

The main agent entry point lives in `app/agent.py`.

## Scaffold and install

```bash
agents-cli scaffold create ambient-expense-agent --prototype --yes
cd ambient-expense-agent
agents-cli install
```

Use `agents-cli install` after scaffolding and whenever dependencies change.

## Local testing

* `agents-cli playground` for interactive checks
* `agents-cli run` for one-off smoke tests
* `agents-cli lint` before debugging behavior

## Evaluation

```bash
agents-cli eval generate
agents-cli eval grade
```

## Deployment readiness

Use `agents-cli scaffold enhance --deployment-target cloud_run` when you are
ready to move beyond local testing.

## Why the loop matters

The local loop keeps the codebase production-shaped, makes it easy to iterate,
and gives you a stable path into evaluation.

## Prompting Antigravity

In the coding-agent flow, describe the intent rather than manually running the
commands yourself. For example, ask it to create the project, install
dependencies, and walk through the generated structure.
