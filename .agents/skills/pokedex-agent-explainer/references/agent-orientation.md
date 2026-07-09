# Agent Orientation

Use this reference when writing or revising the `instruction` field for an ADK
agent.

## What `instruction` Is For

The `instruction` parameter is the main lever for shaping an `LlmAgent`'s
behavior. Use it to define:

* Identity.
* Mission.
* Methodology.
* Limits.
* Few-shot examples.

Treat `instruction` as a prompt-building area, not as a dump of every project
detail.

## Pattern 1: Identity

Use this pattern to define who the agent is:

```md
# Your identity
You are [name], a [role/title] with [experience/specialization].
```

Use it when you want a stable persona, voice, or point of view.

Example:

* The agent sustains the persona "Alex Chen".
* The identity stays consistent even when the request changes.

## Pattern 2: Mission

Use this pattern to define the agent's main goal:

```md
# Your mission
[Main goal] while [quality bar or restriction].
```

Use it when the agent needs a clear objective and a quality standard.

Example:

* The focus of every response is solving technical problems.

## Pattern 3: Methodology

Use this pattern to define a repeatable workflow:

```md
# How you work
1. Recognize
2. Clarify
3. Resolve
4. Verify
```

Use it when you want the agent to follow a consistent process.

Example:

* Recognize the issue.
* Clarify the problem if needed.
* Resolve the request.
* Verify the result.

## Pattern 4: Limits

Use this pattern to define what the agent must not do:

```md
# Your limits
## Scope limits
- Never [out-of-scope action]
## Quality limits
- Never invent [facts]
## Safety limits
- Never [unsafe behavior]
```

Use it when accuracy, scope control, or safety need explicit guardrails.

Example:

* The agent refuses inappropriate requests in a professional way.

## Pattern 5: Few-Shot Examples

Use this pattern to show the desired behavior directly:

```md
# Example interactions
**When [scenario]:**
User: "[input]"
You: "[ideal response]"
```

Use it when the agent needs a specific tone, format, or response shape.

Example:

* The agent reproduces the communication style shown in the examples.

## How The Patterns Work Together

The five patterns work together to create a professional and predictable
behavior profile:

* Identity sets the persona.
* Mission keeps the agent focused on the main objective.
* Methodology gives the agent a stable process.
* Limits protect quality, scope, and safety.
* Examples calibrate tone and response style.

When combined, they help the agent stay consistent even as the input changes.

## Writing Guidance

* Be clear and specific.
* Use Markdown for readability.
* Explain tool usage when tools are available.
* Keep the scope tight.
* Add examples when a pattern needs calibration.

## Reusable Pattern

In many ADK setups, the prompt text lives in configuration or template files
while the final agent is assembled in code.

Use that hybrid pattern when:

* The prompt changes more often than the wiring.
* You want the instruction text to stay easy to review.
* The agent still needs code for routing, dynamic assembly, or tool calls.

When writing the actual prompt text, keep the voice consistent:

* Concise.
* Calm and precise.
* Easy to scan and revise.
* Distinct from a generic assistant tone.

## Source Note

This reference is based on the ADK documentation for simple agents and the
section on guiding the agent with instructions:

https://adk.dev/agents/llm-agents/#guiding-the-agent-instructions-instruction
