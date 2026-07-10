# Safety and plugins

Use this reference when the conversation is about guardrails, policy, plugins,
or cross-cutting behavior controls in ADK.

## Core idea

Safety features help keep agent behavior within boundaries. Plugins extend that
control by offering reusable callback hooks that can apply across agents.

## Main topics

* Safety and security guidance
* Callback-based guardrails
* Plugins
* Policy enforcement across agent behavior

## Why it matters

These features help reduce risk when agents interact with tools, models, or
sensitive data.

## When to use it

Use this reference when the task involves:

* pre-validation;
* policy checks;
* reusable guardrails;
* centralized behavior control.

## Good pattern

1. Prefer the smallest guardrail that solves the problem.
2. Use callbacks for agent-specific checks.
3. Use plugins when the same policy should apply more broadly.

## Source note

Official URLs:
- https://adk.dev/safety/
- https://adk.dev/plugins/
