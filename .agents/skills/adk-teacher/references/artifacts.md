# Artifacts

Use this reference when the conversation is about files or outputs that should
be stored outside the immediate turn.

## Core idea

Artifacts are durable outputs managed by an artifact service and made
available to the runner or invocation context.

## Why it matters

They are useful when the agent needs to keep results, generated files, or
intermediate outputs for later retrieval.

## What to remember

* Artifacts are separate from session state.
* Use the artifact service appropriate to the environment.
* Treat artifacts as stored outputs, not conversation memory.

## Source note

Official URLs:
- https://adk.dev/artifacts/
