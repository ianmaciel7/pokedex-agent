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
* `references/courses.md` for the Agents to Build Agents learning path.
* `references/antigravity-and-agents-cli.md` for the local ADK 2.0 workflow
  lesson about Antigravity, agents-cli, SDD, and review loops.
* `references/adk-learning-map.md` for a reusable map of current ADK learning
  links, doc categories, and update-vs-create decisions.
* `references/setup-and-skill-set.md` for installation, verification, auth,
  skill loading, and session-start patterns.
* `references/local-development-loop.md` for the scaffold-install-test-eval
  loop and project structure.
* `references/managed-agents-module-introduction.md` for the infrastructure-
  first vs code-first module overview.
* `references/managed-agents-sandbox.md` for the secure sandbox, isolation,
  and resource-scoping model.
* `references/managed-agents-interaction-model.md` for control plane vs data
  plane and runtime execution.
* `references/managed-agents-agent-definition.md` for defining durable agents
  on the control plane.
* `references/managed-agents-configuration-environment-data.md` for agent
  configuration, environments, mounts, and cloud storage data.
* `references/managed-agents-tools-and-skills.md` for extending agents with
  tools, MCP, and mounted skills.
* `references/managed-agents-run-and-operate.md` for data-plane runs, typed
  results, state, and production operation.
* `references/managed-agents-execute-and-results.md` for background runs,
  streaming, typed outputs, and usage capture.
* `references/managed-agents-state-and-blueprints.md` for multi-turn state and
  reusable blueprint composition.
* `references/managed-agents-security-and-hardening.md` for production
  security, IAM, containment, and operational hardening.

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
