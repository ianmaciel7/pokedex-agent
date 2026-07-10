# Agent Orientation

Use this reference when writing or revising the `instruction` field for an ADK
agent.

## What It Is

`instruction` is the main way to shape agent behavior. Use it for:

* Identity.
* Mission.
* Workflow.
* Limits.
* Short examples.

Keep it focused. Do not use it to dump every project detail.

## Simple Pattern

Use this order:

1. Say who the agent is.
2. Say what the agent must do.
3. Say how the agent should work.
4. Say what the agent must avoid.
5. Show one or two examples if needed.

## Pattern 1: Identity

Use this when you want a stable persona.

```md
You are [name], a [role] with [specialization].
```

## Pattern 2: Mission

Use this when you want one clear goal.

```md
Your mission is to [goal] while [quality rule].
```

## Pattern 3: Workflow

Use this when the agent should follow the same steps every time.

```md
1. Recognize the problem.
2. Clarify if needed.
3. Solve the request.
4. Verify the result.
```

## Pattern 4: Limits

Use this when you need guardrails.

```md
Never invent facts.
Never go outside the scope.
Never take unsafe action.
```

## Pattern 5: Examples

Use this when tone or format needs to be precise.

```md
When [scenario]:
User: "[input]"
You: "[ideal response]"
```

## Writing Rules

* Be clear and specific.
* Use short sections.
* Keep the scope tight.
* Add examples only when they help.
* Mention tools when the agent should use them.

## Reusable Pattern

In many ADK setups, the prompt lives in config or template files and the
final agent is wired in code.

Use that hybrid pattern when:

* the prompt changes more often than the wiring
* the instruction should be easy to review
* code still needs to handle routing or tool calls

## Source Note

This reference is based on the ADK docs for instruction guidance:

https://adk.dev/agents/llm-agents/#guiding-the-agent-instructions-instruction
