# Agent team

Use this reference when the conversation is about a root agent coordinating
specialist sub-agents.

## Core idea

An agent team lets one agent act as the orchestrator while other agents focus
on narrower responsibilities. The root agent receives the user request, reads
the sub-agents' descriptions, and delegates when another agent is a better fit.

## Why it matters

This pattern keeps complex systems easier to maintain than a single monolithic
agent. Each specialist can stay focused on one domain, which makes prompts
clearer and routing more predictable.

## Common roles

* Root agent: receives the user request and coordinates the team.
* Sub-agent: handles one specialized task or topic.
* Orchestration text: tells the root agent when to delegate and how to choose
  between specialists.

## When to use it

Use an agent team when:

* the app has multiple distinct domains;
* the root agent should route requests automatically;
* the work benefits from specialization;
* you want a clear separation between coordination and task execution.

Skip it when:

* one simple agent can handle the whole task;
* the workflow is purely deterministic;
* there is no meaningful routing decision.

## Good pattern

1. Give the root agent a clear orchestration role.
2. Give each sub-agent a narrow description.
3. State the delegation rules in the root instruction.
4. Keep each sub-agent focused on a single responsibility.

## What to watch for

* Make descriptions specific enough to guide routing.
* Keep the root agent from duplicating specialist behavior.
* Prefer delegation over re-explaining the same logic in multiple places.

## Source note

This reference is based on ADK agent-team guidance and the general multi-agent
pattern described in the official ADK docs.
