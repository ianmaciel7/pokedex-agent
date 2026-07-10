# Collaborative workflows

Use this reference when the conversation is about coordination between agents
or when a task needs multiple agents to work together in a defined sequence.

## Core idea

Collaborative workflows split a larger job into cooperating parts. A coordinator
agent handles the overall flow and delegates to one or more sub-agents, then
collects the results.

## Why it matters

This pattern is useful when a single pass is not enough and the work has
multiple substantial sub-tasks. It makes the control flow easier to reason
about than asking one agent to do everything at once.

## Common shapes

* Sequential collaboration: one sub-task feeds the next.
* Parallel collaboration: independent sub-tasks run side by side.
* Coordinator-led collaboration: one agent delegates, then assembles the final
  answer.

## When to use it

Use collaborative workflows when:

* the task can be broken into clear stages;
* the stages have different specialties;
* the output needs aggregation or comparison;
* you want the orchestration to be explicit.

Skip it when:

* the request is a single lookup;
* one specialist already covers the full scope;
* orchestration would add overhead without value.

## Good pattern

1. Define the coordinator role.
2. Split the task into clear subtasks.
3. Decide whether subtasks run sequentially or in parallel.
4. Return to the coordinator for synthesis and final validation.

## What to watch for

* Keep sub-agent responsibilities narrow.
* Avoid overlap that makes routing ambiguous.
* Make sure the coordinator knows when to stop and synthesize.

## Source note

This reference is based on the ADK workflows and collaboration guidance in the
official documentation.
