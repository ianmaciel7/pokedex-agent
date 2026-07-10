# Strategic Instructions

Use this reference when the agent already has tools, but the prompt needs to
say when and how to use them.

## What It Is

Tools tell the agent what is available. Strategic instructions tell the agent
when to use each tool, how to react, and when to escalate.

## Why It Matters

Without clear instructions, the agent may:

* choose the wrong tool
* use tools in the wrong order
* mishandle errors
* ignore tool results
* skip escalation

## What To Write

Focus on three things:

* tool selection
* result handling
* next step after the call

Do not repeat the full tool implementation. The docstring already covers that.

## Good Patterns

### Tool Selection

Say when to use each tool.

```md
Use `check_order_status` for order lookups.
Use `process_refund` only after confirming eligibility.
Use `lookup_customer` when you need account details.
```

### Result Handling

Say how to react to tool output.

```md
If `check_order_status` returns `not_found`, ask for the correct ID.
If it returns `invalid_format`, explain the expected format.
If it returns success, share the status clearly.
```

### Sequential Workflow

Say which steps must happen in order.

```md
1. Verify the customer.
2. Check the order.
3. Confirm eligibility.
4. Take action or escalate.
```

### Escalation

Say what to do when the tools are not enough.

```md
If a tool fails unexpectedly, do not guess. Explain the issue and escalate.
```

## When To Use It

Use strategic instructions when:

* the agent has more than one tool
* order matters
* errors matter
* escalation matters
* business rules apply

Skip it when:

* the task is a single lookup
* the workflow is obvious
* speed matters more than control

## Source Note

This reference is based on ADK guidance for tool references and tool result
handling.
