# Agent Definition Methods

Use this reference when deciding how to define an ADK agent.

## What It Is

There are two main ways to define an agent:

1. Code-based definition.
2. Config-based definition, also called Agent Config.

Do not call these “agent types.” They are just different ways to assemble the
same kind of agent.

## Code-Based Definition

Define the agent directly in application code.

Use this when you need:

* custom Python logic
* dynamic setup
* conditional routing
* deeper integration with the app
* strong IDE support and tests

Example:

```python
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    name="root_agent",
    model="gemini-flash-latest",
    description="Tells the current time in a city.",
    instruction="Use the get_current_time tool to answer time questions.",
    tools=[get_current_time],
)
```

## Config-Based Definition

Define the agent in a YAML file, such as `agent.yaml`.

Use this when the agent is mostly declarative and easy to describe with:

* `name`
* `model`
* `description`
* `instruction`
* `tools`
* `sub_agents`

Example:

```yaml
name: assistant_agent
model: gemini-flash-latest
description: Answers user questions.
instruction: You are an assistant that helps answer user questions.
```

## When To Use Each One

Use code-based definition when:

* the agent needs custom logic
* the agent changes at runtime
* the wiring is complex
* the agent is part of a larger system

Use config-based definition when:

* the behavior is mostly prompt-driven
* the setup is simple
* non-developers need to review it
* you want a readable declaration

## Hybrid Pattern

Many projects use both.

* YAML holds prompts and agent metadata.
* Python handles wiring, routing, and runtime behavior.

Use this pattern when the prompt changes often but the logic should stay in
code.

## Quick Rule

* If the change is mostly instructions, model names, tools, or sub-agents,
  use config.
* If the change is control flow, conditional behavior, or custom setup, use
  code.

## Gotchas

* Keep `description` focused on routing.
* Keep instructions readable.
* Use code for deterministic logic.
* Avoid huge prompt blobs in YAML.

## Source Note

This reference is based on ADK docs for agent definition and configuration.
