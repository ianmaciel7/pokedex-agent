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

* `references/orientation.md` for instruction-writing patterns.
* `references/definition.md` for code-based vs config-based agent setup.
* `references/config.md` for agent generation settings.
* `references/integration.md` for MCP-based integration with external
  tool servers.
* `references/tools.md` for the jump from basic agents to
  tool-using agents.
* `references/custom-tools.md` for writing custom Python tools for
  business-specific logic.
* `references/orchestration.md` for using instructions and planning to
  coordinate multiple tools effectively.
* `references/strategic-instructions.md` for using tool references in
  agent instructions and handling tool return values well.
* `references/session.md` for session state, `output_key`, `{var}`
  templating, and state namespaces.
* `references/planning.md` for planning, `BuiltInPlanner`, and
  `PlanReActPlanner`.
* `references/structured-data.md` for `input_schema`, `output_schema`,
  and `output_key`.
* `references/a2a.md` for agent-to-agent interoperability and the A2A
  protocol.
* `references/agents.md` for the main agent family, custom agents, routing,
  and workflow-agent concepts.
* `references/team.md` for root agents, orchestrators, and sub-agents.
* `references/workflows-collaboration.md` for collaborative workflows and
  multi-agent coordination patterns.
* `references/workflows.md` for the workflows topic area.
* `references/simple-agents.md` for the core `LlmAgent` concept and the basic
  agent execution modes.
* `references/template-workflows.md` for sequential, loop, parallel, and
  custom template workflows.
* `references/models-for-agents.md` for model selection, providers, and
  routing between models.
* `references/runtime-and-streaming.md` for runtime, web interface, and
  streaming agent behavior.
* `references/runtime.md` for the broader runtime surface, including
  `Runner`, `RunConfig`, command-line, API server, resume, and cancel.
* `references/runner.md` for the `Runner` execution object and run loop.
* `references/integrations.md` for the broader integrations catalog and
  connector landscape.
* `references/mcp.md` for the MCP protocol area.
* `references/tools-custom.md` for the custom tools catalog beyond function
  tools.
* `references/function-tools.md` for Python function tools.
* `references/tool-performance.md` for tool performance guidance.
* `references/action-confirmations.md` for approval steps before tool actions.
* `references/mcp-tools.md` for MCP-based tools.
* `references/openapi-tools.md` for OpenAPI-based tools.
* `references/authentication.md` for securing tool access.
* `references/skills.md` for SkillToolset and the Skills Registry.
* `references/apps.md` for app-facing integrations and agent-to-UI surfaces.
* `references/callbacks.md` for lifecycle hooks and behavior customization.
* `references/callbacks-types.md` for the available callback stages.
* `references/callbacks-patterns.md` for callback design patterns and best
  practices.
* `references/context-and-memory.md` for context, sessions, state, memory,
  caching, and compaction.
* `references/context.md` for the context topic area.
* `references/sessions.md` for sessions, state, memory, and lifecycle
  management.
* `references/session-rewind.md` for rewinding a session.
* `references/session-migrate.md` for migrating sessions.
* `references/events-and-artifacts.md` for event flow and artifact storage.
* `references/events.md` for the events topic area.
* `references/artifacts.md` for artifact storage and retrieval.
* `references/graphs.md` for the graphs topic area.
* `references/graph-workflows.md` for graph routes, data handling, human
  input, and dynamic workflows.
* `references/safety-and-plugins.md` for guardrails, plugins, and security
  considerations.
* `references/deploy.md` for deployment surfaces and targets.
* `references/deploy-agent-runtime.md` for Agent Runtime deployment.
* `references/deploy-cloud-run.md` for Cloud Run deployment.
* `references/deploy-gke.md` for GKE deployment.
* `references/evaluate.md` for evaluation, datasets, metrics, and grading.
* `references/evaluate-criteria.md` for evaluation success criteria.
* `references/evaluate-user-sim.md` for user simulation in evals.
* `references/evaluate-environment-simulation.md` for environment simulation
  in evals.
* `references/evaluate-custom-metrics.md` for custom evaluation metrics.
* `references/get-started.md` for installation and quickstarts.
* `references/grounding.md` for grounding and search grounding.
* `references/observability.md` for logs, metrics, traces, and monitoring.
* `references/optimize.md` for optimization based on evaluation results.
* `references/plugins.md` for plugin hooks and guardrail extensions.
* `references/release-notes.md` for version changes and release notes.
* `references/streaming-dev-guide.md` for the multi-part streaming guide.
* `references/streaming.md` for the streaming docs and live interaction flow.
* `references/tutorials.md` for the tutorial hub and code-with-AI guidance.
* `references/visual-builder.md` for visual builder concepts and workflow
  assembly.
* `references/api-reference.md` for the API reference landing area.
* `references/community.md` for the community and contributing area.
* `references/adk-2.0.md` for the ADK 2.0 landing page.
* `references/tools-limitations.md` for tool limitations and caveats.
* `references/models-google-gemini.md` for Gemini model support.
* `references/models-google-gemma.md` for Gemma model support.
* `references/models-claude.md` for Claude model support.
* `references/models-agent-platform.md` for Agent Platform hosted models.
* `references/models-apigee.md` for Apigee AI Gateway model routing.
* `references/models-routing.md` for model routing.
* `references/models-ollama.md` for Ollama model support.
* `references/models-vllm.md` for vLLM model support.
* `references/models-litellm.md` for LiteLLM routing.
* `references/models-litert-lm.md` for LiteRT-LM support.
* `references/a2a.md` for agent-to-agent interoperability and the A2A
  protocol.
* `references/agents.md` for the main agent family, custom agents, routing,
  and workflow-agent concepts.
* `references/runner.md` for the `Runner` execution object and run loop.
* `references/runconfig.md` for runtime configuration settings.
* `references/command-line.md` for `adk run` and terminal-based runs.
* `references/api-server.md` for the agent API server.
* `references/ambient-agents.md` for event-driven background agents.
* `references/resume.md` for resuming interrupted runs.
* `references/cancel.md` for canceling active runs.
* `references/event-loop.md` for the runtime event loop.
* `references/integrations.md` for the broader integrations catalog and
  connector landscape.
* `references/mcp.md` for the MCP protocol area.
* `references/workflows.md` for the workflows topic area.

Primary docs for planning:

* https://adk.dev/agents/llm-agents/#planning-planner
* https://ai.google.dev/gemini-api/docs/thinking

Related course:

* `references/courses.md`

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
