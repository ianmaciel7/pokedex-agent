# Context, sessions, and memory

Use this reference when the conversation is about how ADK keeps track of a
conversation, what data persists across turns, and how longer-lived knowledge
is retrieved.

## Core idea

ADK separates short-lived conversation data from longer-lived memory and other
context data. That lets an agent keep the current turn manageable while still
remembering useful information across turns when configured to do so.

## Main pieces

* Context: the information available for the current operation.
* Session: the current conversation thread.
* State: data stored inside a session.
* Memory: searchable information that can span sessions.
* Caching: reuse request data where supported.
* Compaction: summarize older context to keep the window small.

## Why it matters

These concepts help with:

* multi-turn continuity;
* long-running tasks;
* memory retrieval;
* cost and latency control;
* context-window management.

## When to use it

Use this reference when you need to decide where data should live or how a
conversation should retain information over time.

## Good pattern

1. Put turn-local data in session state.
2. Use memory for reusable knowledge that should survive across sessions.
3. Use caching or compaction when the model and runtime support it.

## What to watch for

* Keep transient and durable data separate.
* Do not assume in-memory state survives a restart.
* Treat memory retrieval as explicit behavior, not automatic magic.

## Source note

Official URLs:
- https://adk.dev/context/
- https://adk.dev/context/caching/
- https://adk.dev/context/compaction/
- https://adk.dev/sessions/
- https://adk.dev/sessions/memory/
- https://adk.dev/sessions/state/
