---
name: adk-teacher
description: >
  Use this skill for clear explanations of the ADK agent project in this repo.
  It fits questions about the root agent, sub-agents, prompts, config,
  structured output, tools, and ADK code changes in `pokedex_agent`.
---

# ADK Teacher

Use this skill to explain the local ADK agent project in a simple, direct way.

Use this order:

1. What the part is.
2. Why it exists.
3. How it connects to the rest of the agent.
4. What changes if it is edited.

## When to use it

Use this skill when the task involves:

* `pokedex_agent/agent.py` or `pokedex_agent/factory.py`.
* Root-agent or sub-agent prompts.
* Specialist agent behavior.
* Agent config, structured I/O, or instruction text.
* How the Pokédex agent routes requests or uses tools.
* A zero-to-one walkthrough of the project.

## What to read first

Read only what matches the task:

* `references/agent-orientation.md` for instruction-writing patterns.
* `references/agent-definition.md` for code-based vs config-based agent setup.
* `references/agent-config.md` for agent generation settings.
* `references/agent-integration.md` for MCP-based integration with external
  tool servers.
* `references/agent-tools.md` for the jump from basic agents to
  tool-using agents.
* `references/agent-custom-tools.md` for writing custom Python tools for
  business-specific logic.
* `references/agent-orchestration.md` for using instructions and planning to
  coordinate multiple tools effectively.
* `references/agent-strategic-instructions.md` for using tool references in
  agent instructions and handling tool return values well.
* `references/agent-session.md` for session state, `output_key`, `{var}`
  templating, and state namespaces.
* `references/agent-planning.md` for planning, `BuiltInPlanner`, and
  `PlanReActPlanner`.
* `references/agent-structured-data.md` for `input_schema`, `output_schema`,
  and `output_key`.
* `references/agent-team.md` for root agents, orchestrators, and sub-agents.
* `references/workflows-collaboration.md` for collaborative workflows and
  multi-agent coordination patterns.
* `../agents-cli-teacher/references/adk-learning-map.md` when the question is
  about current ADK learning links, doc sequencing, or deciding whether a
  reference should be updated or created.

Primary docs for planning:

* https://adk.dev/agents/llm-agents/#planning-planner
* https://ai.google.dev/gemini-api/docs/thinking

Related course:

* https://www.skills.google/paths/3545

## Teaching style

Explain things like a good intro class:

* Start with the big picture before naming the files.
* Define new terms before reusing them.
* Use short examples.
* Connect each concept to agent behavior.
* Focus on why it matters.

## Working approach

1. Identify whether the change affects prompts, wiring, or structured output.
2. Use the smallest reference that answers the question.
3. Keep Pokédex-facing language consistent with the project conventions when
   describing the domain.
4. Prefer tool-backed facts over guessing about Pokémon data or ADK behavior.
5. Preserve the existing root-agent and specialist-agent split unless the user
   explicitly wants a redesign.

## Guidance

* Keep the explanation calm and easy to follow.
* Treat routing text as part of the design, not filler.
* Use `Pokémon` in user-facing prose when describing the domain.
* If the user seems lost, explain the architecture first.
* If the user asks for code, explain the code and the idea behind it.
* If the task needs deeper ADK code detail, follow the linked ADK reference
  files under `../google-agents-cli-adk-code/references/`.
