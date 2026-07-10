# Runtime and streaming

Use this reference when the conversation is about running ADK agents,
interacting with the runtime, or enabling streaming behavior.

## Core idea

The runtime is where the agent actually executes. Streaming adds low-latency,
incremental interaction for text, audio, or other supported modalities.

## Main topics

* Agent runtime
* Web interface
* Streaming agent behavior
* Streaming and live interaction patterns

## Why it matters

Runtime choices affect:

* how you test the agent locally;
* how users interact with it;
* how quickly partial results appear;
* whether multimodal streaming is needed.

## When to use it

Use this reference when the question is about execution, local interaction, or
real-time response modes.

## Good pattern

1. Pick the simplest runtime mode that meets the need.
2. Use streaming only when incremental output helps the experience.
3. Keep the runtime model aligned with the deployment target.

## Source note

Official URLs:
- https://adk.dev/runtime/
- https://adk.dev/get-started/streaming/
- https://adk.dev/streaming/
