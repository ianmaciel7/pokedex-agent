# Workflow: Antigravity, vibecoding, and spec-driven development

Use this reference when the conversation is about writing agent logic through
Antigravity, reviewing generated code, or starting from a specification before
code.

## Core idea

Antigravity acts as the agentic IDE that writes and edits code from natural
language design.
agents-cli provides lifecycle knowledge, conventions, and ADK guidance so the
generated code stays closer to the correct API surface from the start.

Together, they help you focus on:

* what the agent should do;
* why the behavior exists;
* how to validate the generated structure;
* when to correct the implementation before moving on.

## Vibecoding

The lesson frames the developer as the architect:

1. Describe the behavior in natural language.
2. Let the tool generate the implementation.
3. Review the resulting structure.
4. Correct any mismatch before continuing.

This works best when the prompt is specific, behavioral, and explicit about
system boundaries.

## Spec-driven development

Write a formal specification before code when the task has meaningful routing,
security, or multi-step behavior.

Good specs:

* define routing rules;
* make it clear what should never reach the LLM;
* document success, failure, and edge-case scenarios;
* serve as the single source for regeneration.

## Pattern example

For an expense agent:

* low-value expenses may be approved automatically;
* high-value expenses may require LLM analysis;
* risky or sensitive cases may require human review;
* the threshold logic should live in code, not in the model.

## Review loop

After the tool generates the flow:

1. ask for a step-by-step explanation;
2. compare it with the original intent;
3. correct any differences;
4. only then move to the next step.

## How to use this reference

Use this material when the question involves:

* how Antigravity and agents-cli complement each other;
* how to write better prompts for ADK workflows;
* how to think about SDD for agents;
* how to review generated code before trusting it.

## Reference map

Use local references first, then compare them with the official ADK site when
you need to confirm page names or the current learning order.

Suggested reading order:

1. ADK home: https://adk.dev/
2. Get started: https://adk.dev/get-started/
3. Build your agent with ADK: https://adk.dev/tutorials/
4. Code with AI: https://adk.dev/tutorials/coding-with-ai/
5. Agent team: https://adk.dev/tutorials/agent-team/
6. Workflows: https://adk.dev/workflows/
7. Collaborative workflows: https://adk.dev/workflows/collaboration/
8. Agents: https://adk.dev/agents/
9. LLM agents: https://adk.dev/agents/llm-agents/
10. Evaluate: https://adk.dev/evaluate/
11. Agents CLI deploy: https://adk.dev/deploy/agent-runtime/agents-cli/

When reviewing a topic, check:

* whether the local reference already covers the concept;
* whether the official site has a newer page name or structure;
* whether the gap is a small edit or a new reference file.

Prefer updating an existing reference when the concept is already covered.
Create a new reference when the topic crosses into a different ADK area or the
material would make the current file too broad.
