# Models for agents

Use this reference when the conversation is about choosing, routing, or
configuring models for ADK agents.

## Core idea

ADK can work with multiple model providers and routing strategies. The main
question is not just which model exists, but which model fits the task.

## Common topics

* Gemini
* Gemma
* Claude
* Agent Platform hosted models
* Apigee AI Gateway
* Model routing
* Ollama
* vLLM
* LiteLLM
* LiteRT-LM

## Why it matters

Model choice affects:

* latency;
* cost;
* capability;
* deployment fit;
* whether routing or fallback logic is needed.

## When to use it

Use this reference when the task is about model selection, provider support,
or how to route between models.

## Good pattern

1. Choose the simplest model that fits the task.
2. Route only when there is a clear reason.
3. Keep provider-specific details out of the task logic when possible.

## Source note

Official URLs:
- https://adk.dev/agents/models/
