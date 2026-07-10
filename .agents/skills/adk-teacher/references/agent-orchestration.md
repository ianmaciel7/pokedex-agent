# Tool Orchestration

Use this reference when an agent already has tools, but needs better
instructions to use them in the right order, with the right checks, and with
better error handling.

## Introduction

From individual tools to coordinated systems.

Your journey:

* Part 1: understand tools fundamentally and build your first tool-enabled
  agent.
* Part 2: use production-ready built-in tools such as Google Search and code
  execution.
* Part 3: write custom Python tools for business-specific logic.
* Part 4: coordinate multiple tools effectively for real-world scenarios.

The shift in this part is:

* tools alone are not enough
* you also need strategic instructions that tell the agent when, how, and in
  what order to use them

## The Problem

Tools without guidance.

Suppose you have several tools:

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

* tool selection mistakes: the agent may call `process_refund` before checking
  whether the order exists
* poor error handling: the agent may not know what to do when a tool fails
* wrong ordering: the agent may call tools in a logically bad sequence
* ignored results: the agent may not use the tool output correctly
* no escalation path: the agent may get stuck when the task exceeds its
  capabilities

The root issue is simple:

* tools need instructions that explain when, how, and in what order to use
  them

## Why Instructions Matter

Good orchestration instructions help the agent:

* pick the right tool
* use tools in the right sequence
* handle failures gracefully
* decide when to continue and when to stop
* avoid acting on incomplete information

Think of the instruction as the control policy for the toolset.

## What Good Orchestration Looks Like

The agent should not just know that tools exist.

It should know:

* which tool to use first
* what information must be gathered before taking action
* what to do when a tool returns an error
* when to ask the user for more information
* when to escalate or stop

Example pattern:

```md
# How you work
1. Look up the customer.
2. Check the order status.
3. Only process a refund if the order is eligible.
4. If a tool returns an error, explain the issue clearly.
5. If the request is outside your authority, escalate to a human supervisor.
```

## Practical Guidance

Use orchestration instructions when the agent needs to:

* coordinate several tools
* follow a business process
* respect ordering constraints
* avoid risky actions
* know when to escalate

Good orchestration instructions are:

* specific
* short enough to scan
* written in a stepwise format
* aligned with the business workflow

## What To Write In The Prompt

A useful orchestration prompt often includes:

* the agent's role
* the normal workflow
* the decision order for tools
* error handling rules
* escalation rules

Example:

```md
# Your mission
Help customers with order issues while avoiding unnecessary refunds.

# How you work
1. Verify the customer.
2. Check the order status.
3. Confirm whether the request is eligible for action.
4. Use the smallest necessary tool.
5. Escalate if the case is ambiguous or restricted.
```

## When To Use This Pattern

Use orchestration-focused instructions when:

* the agent has more than one tool
* tool order matters
* bad sequencing could cause mistakes
* the workflow has approval or escalation rules
* the agent must reason about tool results before acting

Skip heavy orchestration when:

* the task is a single-step lookup
* the workflow is obvious
* speed matters more than multi-step control

## Source Note

This reference is based on ADK prompt-writing guidance and the practical
need to coordinate multiple tools in real workflows.
