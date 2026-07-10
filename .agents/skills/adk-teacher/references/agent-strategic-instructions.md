# Strategic Instructions

Use this reference when the agent already has tools, but the prompt needs to
tell it when to use each tool, how to react to results, and when to escalate.

## Introduction

From tool availability to tool guidance.

Your journey:

* Part 1: understand tools fundamentally and build your first tool-enabled
  agent.
* Part 2: use built-in tools such as Google Search and code execution.
* Part 3: write custom Python tools for business-specific logic.
* Part 4: coordinate tool use with clear, strategic instructions.

The shift in this part is:

* tools tell the agent what it can do
* instructions tell the agent when, how, and in what order to do it

## The Problem

Tools without guidance.

Suppose you have these tools:

```python
from google.adk.agents import LlmAgent


def check_order_status(order_id: str) -> dict:
    """Check the status of an order."""
    ...


def process_refund(order_id: str, amount: float) -> dict:
    """Process a refund for an order."""
    ...


def lookup_customer(email: str) -> dict:
    """Look up customer information."""
    ...


agent = LlmAgent(
    model="gemini-2.5-flash",
    instruction="You are a customer service agent.",
    tools=[check_order_status, process_refund, lookup_customer],
)
```

That instruction is too vague.

What can go wrong:

* the agent may choose the wrong tool
* the agent may use tools in the wrong order
* the agent may mishandle errors
* the agent may ignore tool output
* the agent may not know when to escalate

The root issue is simple:

* tools need instructions that explain when, how, and in what order to use
  them

## What Strategic Instructions Do

Good strategic instructions give the agent:

* tool selection guidance
* result-handling guidance
* sequencing guidance
* escalation guidance
* error-handling guidance

They should focus on:

* when to use a tool
* how to use it
* what to do after the call

They should not repeat the full tool implementation. The docstring already
covers what the tool does.

## Pattern 1: Tool Selection Guidance

Tell the agent when to use each tool.

Example:

```md
You are a customer support agent.

Tool selection guide:
- Use `check_order_status` when the customer asks about an order.
- Use `process_refund` when the customer requests a refund.
- Use `lookup_customer` when you need account information.
- Always verify the relevant information before taking action.
```

This reduces tool confusion and makes the agent more consistent.

## Pattern 2: Result Handling

Tell the agent how to interpret different tool results.

Example:

```md
When using `check_order_status`:
1. Call the tool with the order ID.
2. If the result status is `success`:
   - Tell the customer the current order status.
   - Include tracking details if available.
3. If the result status is `error` and the error type is `not_found`:
   - Ask the customer to verify the order ID.
   - Offer to search by email instead.
4. If the result status is `error` and the error type is `invalid_format`:
   - Explain the correct order ID format.
   - Ask for the correct format.
```

This helps the agent respond to tool output instead of treating every result
the same way.

## Pattern 3: Sequential Workflows

Use step-by-step instructions when several tools must be called in order.

Example:

```md
For refund requests:
1. First use `check_order_status` to verify that the order exists.
2. If the order is not found, stop and ask for the correct order ID.
3. If the order exists, use `process_refund` with the order ID and reason.
4. If the refund succeeds, confirm the refund amount and reference number.
5. If the refund is denied, explain why and offer escalation.
```

This prevents the agent from skipping required checks.

## Pattern 4: Escalation Rules

Tell the agent what to do when tools cannot solve the problem.

Example:

```md
If a tool returns an unexpected error:
- Apologize clearly.
- Do not guess.
- Do not invent a workaround.
- Escalate to a human supervisor.
```

Escalation rules are especially important when the action affects customers,
money, or account access.

## Pattern 5: Structured Prompt Sections

A practical agent prompt often has sections like:

```md
# Your mission
Help customers resolve order issues safely and accurately.

# Tool selection
- Use `check_order_status` for order lookups.
- Use `lookup_customer` when you need account details.
- Use `process_refund` only after confirming eligibility.

# Workflow
1. Verify the customer.
2. Check the order.
3. Decide whether the order can be refunded.
4. Take action or escalate.

# Error handling
- `not_found`: ask the user to verify the ID.
- `invalid_format`: explain the expected format.
- `permission_denied`: escalate immediately.
```

That structure makes the prompt easier to scan and revise.

## Why This Matters

Strategic instructions help the agent:

* choose the right tool
* use tools in the right sequence
* handle failures gracefully
* integrate results correctly
* escalate when needed

Without them, the model may know what the tools do, but not how to use them
reliably in a real workflow.

## Agent As A Tool

When a subtask needs its own reasoning and workflow, you may use another
agent as a tool.

That is useful when:

* the subtask needs specialized judgment
* the subtask needs different instructions
* the subtask has its own workflow

In that case, the main agent can delegate to a specialist agent instead of
calling only low-level function tools.

## When To Use This Pattern

Use strategic instructions when:

* the agent has more than one tool
* tool order matters
* error handling matters
* escalation matters
* the workflow has business rules

Skip heavy instruction design when:

* the task is a single-step lookup
* the workflow is obvious
* speed matters more than detailed control

## Source Note

This reference is based on ADK guidance for referencing tools in agent
instructions and handling tool return values clearly.
