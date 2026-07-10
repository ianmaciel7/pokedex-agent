# Runner

Use this reference when the conversation is about the ADK `Runner` object and
the code that executes agent turns.

## Core idea

`Runner` is the execution coordinator that receives an agent, a session
service, and runtime configuration, then drives the run loop.

## Why it matters

It is the bridge between the agent definition and the actual runtime
interaction.

## Main points

* `Runner` executes turns.
* It works with session services and invocation context.
* It is used by `run_async()` and `run_live()`.

## Source note

Official URLs:
- https://adk.dev/runtime/event-loop/
- https://adk.dev/runtime/runconfig/
