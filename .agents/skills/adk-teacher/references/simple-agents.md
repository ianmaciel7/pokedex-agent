# Simple agents

Use this reference when the conversation is about the core `LlmAgent` concept
and the simplest way to build an agent in ADK.

## Core idea

An `LlmAgent` is the basic agent building block. It combines a model,
instructions, and optionally tools so the model can reason and act.

## Why it matters

This is the foundation for more advanced patterns such as agent teams, tool
usage, planning, and workflows.

## Main ideas

* The agent interprets instructions and context.
* The model chooses how to respond.
* Tools extend the agent with external capabilities.
* Execution mode affects whether the agent chats, works once, or behaves as a
  task agent.

## When to use it

Use this reference when the topic is the base agent abstraction or how a
single agent behaves before you add orchestration.

## Good pattern

1. Start with a simple agent.
2. Add tools only when the agent needs them.
3. Move to workflows or sub-agents when the problem grows.

## Source note

Official URLs:
- https://adk.dev/agents/llm-agents/
