# Tool Orchestration

Use this reference when an agent has tools but needs better guidance on how to
use them.

## What It Is

Tool orchestration is the instruction layer that tells the agent:

* which tool to use first
* what to check before acting
* how to handle errors
* when to stop or escalate

## Why It Matters

Without clear guidance, the agent may:

* choose the wrong tool
* use tools in the wrong order
* ignore tool results
* fail to escalate when needed

## Good Pattern

Write the workflow as short steps.

Example:

```md
1. Look up the customer.
2. Check the order status.
3. Only process a refund if the order is eligible.
4. Explain errors clearly.
5. Escalate when the request is outside your authority.
```

## What To Include

A good orchestration prompt usually has:

* the agent's role
* the normal workflow
* the tool order
* error rules
* escalation rules

Example:

```md
Help customers with order issues.

1. Verify the customer.
2. Check the order.
3. Confirm eligibility.
4. Use the smallest necessary tool.
5. Escalate if the case is unclear or restricted.
```

## When To Use It

Use orchestration instructions when:

* the agent has more than one tool
* order matters
* failures need special handling
* escalation is part of the process

Skip it when:

* the task is a single lookup
* the workflow is obvious
* speed matters more than control

## Source Note

This reference is based on ADK prompt-writing guidance for multi-tool flows.
