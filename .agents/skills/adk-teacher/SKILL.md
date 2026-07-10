---
name: adk-teacher
description: >
  Use this skill when you want a teacher-like explanation of the ADK agent
  project in this repo. Trigger it for questions about the root agent,
  sub-agents, prompt text, agent configuration, structured output, tool usage,
  or ADK code changes for the `pokedex_agent` package. It is useful when the
  user wants an overview, a conceptual walkthrough, or a step-by-step
  explanation of how the agent works.
---

# ADK Teacher

Use this skill when you need to explain the local ADK agent project in a clear,
classroom-style way.

Think of the explanation in this order:

1. What the part is.
2. Why it exists.
3. How it connects to the rest of the agent.
4. What changes if it is edited.

## When to use it

Use this skill when the task involves any of the following:

* Updating `pokedex_agent/agent.py` or `pokedex_agent/factory.py`.
* Changing root-agent or sub-agent prompts.
* Adding or revising specialist agent behavior.
* Working on agent config, structured I/O, or instruction text.
* Explaining how the Pokédex agent routes requests or uses tools.
* Walking someone through the project from zero, as if teaching the system.

## What to read first

Read these references based on the task:

* `references/agent-orientation.md` for instruction-writing patterns.
* `references/agent-definition.md` for code-based vs config-based agent setup.
* `references/agent-config.md` for agent generation settings.
* `references/agent-session.md` for session state, `output_key`, `{var}`
  templating, and state namespaces.
* `references/agent-planning.md` for planning, `BuiltInPlanner`, and
  `PlanReActPlanner`.
* `references/agent-structured-data.md` for `input_schema`, `output_schema`,
  and `output_key`.

Primary docs for planning and thinking:

* https://adk.dev/agents/llm-agents/#planning-planner
* https://ai.google.dev/gemini-api/docs/thinking

## Teaching style

Explain things like a professor would in a good intro class:

* Start with the big picture before naming the files.
* Define unfamiliar terms before using them again.
* Use short examples to make the idea concrete.
* Connect each concept back to the agent's behavior.
* Prefer "why this matters" over bare technical listing.

## Working approach

1. Identify whether the change affects prompts, wiring, or structured output.
2. Use the smallest reference that answers the question.
3. Keep Pokédex-facing language consistent with the project conventions when
   describing the domain.
4. Prefer tool-backed facts over guessing about Pokémon data or ADK behavior.
5. Preserve the existing root-agent and specialist-agent split unless the user
   explicitly wants a redesign.

## Guidance

* Keep the explanation calm, friendly, and easy to follow.
* Treat routing text as part of the agent design, not as filler.
* Use `Pokémon` in user-facing prose when describing the domain.
* If the user seems lost, slow down and explain the architecture first.
* If the user asks for code, explain the code and the idea behind it.
* If the task needs deeper ADK code detail, follow the linked ADK reference
  files under `../google-agents-cli-adk-code/references/`.
