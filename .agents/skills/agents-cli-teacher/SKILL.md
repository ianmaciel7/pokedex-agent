---
name: agents-cli-teacher
description: >
  Use this skill for clear explanations of the agents-cli workflow in this
  repo, including scaffold, build, eval, deploy, publish, observe, command
  usage, flags, and how those phases map to local ADK projects.
---

# Agents CLI Teacher

Use this skill to explain agents-cli concepts and how they fit this
repository.

Use this order:

1. What the command or phase is.
2. Why it exists.
3. How it fits into the ADK lifecycle.
4. What changes if options or files are edited.

## When to use it

Use this skill when the task involves:

* `agents-cli info`, `scaffold`, `run`, `eval`, `deploy`, `publish`, or
  observability commands.
* Reading or explaining `.agents-cli-spec.md`.
* Mapping user terms to agents-cli terminology.
* Choosing between scaffold, build, eval, deploy, publish, or observe phases.
* Teaching the repo's agents-cli conventions.

## What to read first

Read only what matches the task:

* `../google-agents-cli-workflow/SKILL.md` for the end-to-end lifecycle.
* `../google-agents-cli-scaffold/SKILL.md` for project creation and enhancement.
* `../google-agents-cli-adk-code/SKILL.md` for ADK code patterns.
* `../google-agents-cli-eval/SKILL.md` for evaluation and grading.
* `../google-agents-cli-deploy/SKILL.md` for deployment targets.
* `../google-agents-cli-observability/SKILL.md` for logs and traces.
* `../adk-teacher/SKILL.md` when the question is about ADK structure rather
  than the CLI.
* `references/courses.md` for courses and learning paths.
* `references/setup.md` for installation and local setup.
* `references/workflow.md` for vibecoding and spec-driven development.
* `references/local-development-loop.md` for the standard local development
  loop.
* `references/managed-agents.md` for the managed runtime lessons.

## Teaching style

Explain things like a practical walkthrough:

* Start with the big picture before naming commands.
* Define terms before reusing them.
* Use short examples when a command or flag is easy to confuse.
* Connect each phase to the agent's behavior or lifecycle.
* Keep the explanation focused on the user's immediate goal.

## Working approach

1. Identify whether the task is about understanding, scaffolding, building,
   testing, deployment, or monitoring.
2. Use the smallest reference that answers the question.
3. Prefer repo-specific facts over generic agents-cli descriptions.
4. Preserve existing project structure unless the user explicitly wants a
   redesign.
