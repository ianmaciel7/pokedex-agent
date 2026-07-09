# Agent Planning

Use this reference when explaining or configuring ADK planning for an agent.
The goal is to show when planning helps, which planner to choose, and how to
configure thinking in a way that fits the task.

## What Planning Is For

Planning helps an `LlmAgent` work through problems that need several steps,
tradeoff analysis, or deeper reasoning before the final answer.

Use planning when the task involves:

* Multi-step problem solving.
* Comparing options and weighing pros and cons.
* Strategic decisions with costs, risks, or constraints.
* Debugging or inspecting how the agent reasons.

Skip planning when the task is:

* A simple factual lookup.
* A short, direct question.
* A single-step response.
* A case where speed matters more than analysis.

## The Main Planner Choice

For this project, the primary option is `BuiltInPlanner`.
It is the best fit when the agent uses Gemini models with native reasoning
support.

Use `PlanReActPlanner` only when you need a more explicit plan-action-reasoning
structure for models that do not have built-in reasoning.

### BuiltInPlanner

`BuiltInPlanner` lets the model use its native planning and reasoning
capabilities before producing the final response.

Best for:

* Gemini models with built-in reasoning support.
* Natural multi-step reasoning.
* Problems where you want deeper analysis without forcing a rigid output shape.
* Debugging, especially when `include_thoughts=True`.

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
    instruction="Resolva problemas complexos de forma sistemática.",
)
```

### PlanReActPlanner

`PlanReActPlanner` is useful when the model does not have native reasoning and
you want a more explicit sequence such as plan, action, reasoning, and final
answer.

Best for:

* Non-Gemini models.
* Tool-heavy workflows that benefit from explicit stages.
* Tasks that need a strict reasoning structure in the output.

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

When using `BuiltInPlanner`, the main tuning knobs are in
`google.genai.types.ThinkingConfig`.

* `thinking_budget` controls how many tokens the model may spend on reasoning.
* `include_thoughts` controls whether reasoning details are exposed in the
  response.

Common patterns:

```python
from google.genai import types

debug_config = types.ThinkingConfig(
    include_thoughts=True,
    thinking_budget=1024,
)

quiet_config = types.ThinkingConfig(
    include_thoughts=False,
    thinking_budget=512,
)
```

Practical guidance:

* Use a smaller budget for simple or time-sensitive tasks.
* Use a larger budget for complex analysis, planning, or tradeoff-heavy
  decisions.
* Turn on `include_thoughts` when you want to inspect reasoning during
  development or debugging.

## How Planning Changes Behavior

Planning usually makes the agent better at:

* Breaking a problem into parts.
* Considering more than one scenario.
* Quantifying tradeoffs instead of guessing.
* Producing recommendations with more context.

It does not mean every answer should be long. A well-configured planner should
still answer simple questions directly when the task is simple.

## Example Mental Model

For a question like “Should I buy or rent a car if I drive 80 km per day?”, a
planning-enabled agent should:

1. Estimate annual usage.
2. Compare cost, limits, and long-term impact.
3. Check the risk of mileage overages.
4. Give a recommendation with a clear exception case if needed.

That is the kind of stepwise reasoning planning is meant to unlock.

## Recommended Rule Of Thumb

* Use `BuiltInPlanner` for Gemini-based agents that need deeper reasoning.
* Use `PlanReActPlanner` when the model needs an explicit plan-action format.
* Avoid planning for short, factual, or urgent requests.

## Source Note

This reference is based on:

* https://adk.dev/agents/llm-agents/#planning-planner
* https://ai.google.dev/gemini-api/docs/thinking
