# Events and artifacts

Use this reference when the conversation is about execution events or stored
artifacts produced by an ADK agent.

## Core idea

Events describe what happened during execution. Artifacts are stored outputs
that can be retrieved later through an artifact service.

## Why it matters

These concepts help when you need to:

* inspect agent execution;
* persist generated files or outputs;
* separate conversational state from durable artifacts;
* understand what the runtime produced.

## Main distinction

* Events belong to the execution trace.
* Artifacts belong to stored outputs managed by an artifact service.

## When to use it

Use this reference when the task involves tracing, storage, or outputs that
should outlive a single model turn.

## Good pattern

1. Keep the event stream for observation and debugging.
2. Store durable outputs as artifacts when they need retrieval later.
3. Use the artifact service appropriate for the environment.

## Source note

Official URLs:
- https://adk.dev/events/
- https://adk.dev/artifacts/
