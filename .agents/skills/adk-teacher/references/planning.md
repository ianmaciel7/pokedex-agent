# Agent Planning

Use this reference when an agent needs multi-step reasoning.

## What It Is

Planning helps the agent work through problems that need:

* several steps
* tradeoff analysis
* deeper reasoning
* debugging or inspection

## When To Use It

Use planning for:

* multi-step problem solving
* option comparison
* cost, risk, or constraint analysis
* reasoning you want to inspect

Skip planning for:

* simple lookups
* short direct questions
* single-step responses
* urgent tasks where speed matters more

## Main Choice

Use `BuiltInPlanner` for Gemini models with native reasoning.

Use `PlanReActPlanner` when you need an explicit plan-action structure.

## `BuiltInPlanner`

Best for natural reasoning and deeper analysis.

Example:

```python
from google.adk.agents import LlmAgent
from google.adk.planners import BuiltInPlanner
from google.genai import types

planning_agent = LlmAgent(
    model="gemini-2.5-flash",
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True,
            thinking_budget=1024,
        )
    ),
    instruction="Solve complex problems step by step.",
)
```

## `PlanReActPlanner`

Best when the model needs explicit plan, action, and reasoning stages.

Example:

```python
from google.adk.agents import LlmAgent
from google.adk.planners import PlanReActPlanner

tool_agent = LlmAgent(
    model="your-model",
    planner=PlanReActPlanner(),
)
```

## Thinking Config

Use `google.genai.types.ThinkingConfig` to tune reasoning.

* `thinking_budget` controls how much reasoning space the model gets.
* `include_thoughts` controls whether reasoning is exposed.

## Quick Rule

* Use `BuiltInPlanner` for Gemini agents with deeper reasoning needs.
* Use `PlanReActPlanner` when you need a strict reasoning format.
* Skip planning for short, factual, or urgent requests.

## Source Note

This reference is based on:

* https://adk.dev/agents/llm-agents/#planning-planner
* https://ai.google.dev/gemini-api/docs/thinking

## Source note

Official URLs:
- https://adk.dev/agents/llm-agents/#planning-planner
- https://ai.google.dev/gemini-api/docs/thinking
