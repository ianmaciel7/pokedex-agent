# Template workflows

Use this reference when the conversation is about reusable workflow patterns
such as sequential, loop, parallel, or custom execution.

## Core idea

Template workflows provide predefined orchestration patterns for running one or
more sub-agents in a predictable structure.

## Main patterns

* Sequential workflow: run sub-agents in a fixed order.
* Loop workflow: repeat a step or set of steps until a condition is met.
* Parallel workflow: run independent work concurrently.
* Custom template workflows: define a custom control flow when built-ins are
  not enough.

## Why it matters

These patterns are helpful when the flow itself is part of the design and
should not be left to chance.

## When to use it

Use template workflows when the order of execution, repetition, or
concurrency matters.

Skip them when a single agent or a simple delegation pattern is enough.

## Good pattern

1. Choose the simplest workflow that matches the task.
2. Use sequential flows when one result depends on the previous step.
3. Use parallel flows only for independent work.
4. Use custom workflows only when the built-ins do not fit.

## Source note

Official URLs:
- https://adk.dev/agents/workflow-agents/sequential-agents/
- https://adk.dev/agents/workflow-agents/loop-agents/
- https://adk.dev/agents/workflow-agents/parallel-agents/
- https://adk.dev/agents/custom-agents/
