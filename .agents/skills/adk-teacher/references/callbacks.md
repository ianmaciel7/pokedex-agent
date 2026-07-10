# Callbacks

Use this reference when the conversation is about lifecycle hooks that let an
agent observe, customize, or control behavior at specific execution points.

## Core idea

Callbacks are hooks around agent execution. They let you inspect inputs, adjust
outputs, validate tool use, and apply policy without rewriting the core agent.

## Why it matters

Callbacks are useful when you need:

* validation before or after a tool call;
* auditing or logging around model and tool execution;
* policy enforcement;
* small behavior changes that should not live inside the main prompt.

## Common uses

* pre-validation for tool inputs;
* post-processing for tool or model outputs;
* request filtering;
* error handling and observation;
* guardrails for sensitive actions.

## When to use it

Use callbacks when the behavior should happen around execution rather than
inside the agent prompt.

Skip them when a plain tool, prompt instruction, or workflow step already
covers the need.

## Good pattern

1. Identify the execution point you need.
2. Keep the callback small and focused.
3. Use it for control or observation, not for business logic that belongs in a
   tool.

## Source note

Official URLs:
- https://adk.dev/callbacks/
