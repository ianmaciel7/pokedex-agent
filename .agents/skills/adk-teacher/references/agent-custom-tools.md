# Custom Tools

Use this reference when the agent needs business-specific logic that is not
covered by built-in ADK tools or an existing MCP server.

## Introduction

From integrated tools to custom tools.

Your journey:

* Part 1: understand tools fundamentally and build your first tool-enabled
  agent.
* Part 2: use production-ready built-in tools such as Google Search and code
  execution.
* Part 3: connect to MCP servers when an external tool already exists.
* Part 4: write custom Python tools for your own business logic.

The shift in this part is:

* instead of importing a ready-made tool,
* you write a Python function and ADK turns it into a tool the agent can use.

## The Problem

Built-in tools are excellent for common tasks, but they do not know your
business.

For example, your company may need tools to:

* calculate shipping costs for your own catalog
* query inventory in your private database
* process refunds in your internal system
* validate loyalty points in your rewards program
* schedule meetings in your own calendar workflow
* check order status in your e-commerce platform

Generic tools do not carry your product rules, pricing policies, or internal
system access.

That creates a gap:

* built-in tools cover universal needs
* custom tools cover business-specific needs

## Why Generic Tools Are Not Enough

Problems with generic solutions:

* No business context: they do not know your products, pricing, or policies.
* No access to your systems: they cannot magically reach proprietary APIs or
  databases.
* One-size-fits-all behavior: they are not shaped around your workflows.
* Limited customization: you cannot change how the built-in tool behaves.

The root issue is simple:

* every business has its own logic, data, and systems
* that often requires custom integration

## What Custom Tools Are

In ADK, a custom tool is usually a Python function that the framework exposes
to the agent.

When you add that function to an agent's `tools` list, ADK automatically
wraps it as a `FunctionTool`.

ADK uses the function's:

* name
* docstring
* parameter types
* return type

to help the model understand how to call it.

Custom tools are best when the logic is:

* deterministic
* business-specific
* reusable across turns
* easier to maintain in code than in a prompt

## How ADK Uses Custom Tools

The usual pattern is:

1. You write a Python function.
2. You add it to the agent's `tools` list.
3. ADK makes it available to the model.
4. The model decides when to call it.
5. The function runs and returns a result.

Example:

```python
from google.adk.agents import LlmAgent


def calculate_shipping_cost(weight_kg: float, country: str) -> dict:
    """Calculate shipping cost for the business.

    Args:
        weight_kg (float): Weight of the package in kilograms.
        country (str): Destination country.

    Returns:
        dict: A status payload with the shipping result.
    """
    rates = {"usa": 10, "canada": 12, "uk": 15}
    country_key = country.lower()
    if country_key not in rates:
        return {
            "status": "error",
            "error_message": f"We do not ship to {country}.",
        }

    cost = weight_kg * rates[country_key]
    return {
        "status": "success",
        "cost_usd": round(cost, 2),
        "country": country,
    }


shipping_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="shipping_agent",
    instruction="You help users with shipping-related questions.",
    tools=[calculate_shipping_cost],
)
```

## What The LLM Sees

The model does not see raw Python implementation details first.

It sees the tool metadata that ADK derives from the function:

* the tool name
* the description from the docstring
* the parameter list and types
* the expected return shape

That metadata helps the model decide:

* when to call the tool
* what arguments to pass
* how to interpret the result

## Why Signatures Matter

The function signature is important because it shapes the schema ADK gives to
the LLM.

### Good names

Use descriptive verb-noun names:

```python
def get_shipping_cost(weight: float, destination: str) -> dict:
    """Return the shipping cost for a package."""
    ...


def calculate_loyalty_points(purchase_amount: float) -> dict:
    """Calculate loyalty points earned from a purchase."""
    ...


def search_available_flights(destination: str, date: str) -> dict:
    """Search for flights to a destination."""
    ...
```

### Bad names

Avoid vague names:

```python
def process(data: float) -> dict:
    ...


def do_stuff(x: str) -> dict:
    ...


def handler(amount: float) -> dict:
    ...
```

## Type Hints Matter

Type hints tell ADK what the LLM should provide.

Use types that are easy to serialize and understand:

* `str`
* `int`
* `float`
* `bool`
* `list`
* `dict`

Avoid complex custom objects when a simple JSON-friendly type is enough.

Good:

```python
def book_flight(destination: str, departure_date: str, passengers: int) -> dict:
    ...
```

Less ideal:

```python
from datetime import datetime


def book_flight(destination: str, departure_date: datetime) -> dict:
    ...
```

## Required Parameters Are Safer

Prefer required parameters when possible.

ADK guidance warns that default values are not always used reliably by the
model, so required arguments are usually clearer.

Good:

```python
def book_flight(destination: str, date: str, passengers: int) -> dict:
    """Book a flight."""
    ...
```

Less ideal:

```python
def search_flights(
    destination: str,
    max_price: float = 1000.0,
    class_type: str = "economy",
) -> dict:
    """Search flights."""
    ...
```

## Docstrings Matter

The docstring is sent to the LLM as the tool description.

Write it like a concise mini-spec:

* what the tool does
* when to use it
* what the parameters mean
* what the return value looks like

Example pattern:

```python
def tool_name(param1: type1, param2: type2) -> dict:
    """Short summary of what the tool does.

    Optional context about when to use it.

    Args:
        param1 (type1): Description of param1.
        param2 (type2): Description of param2.

    Returns:
        dict: Description of the response shape.
    """
```

## Return Dictionaries With Status

Prefer returning a Python dictionary.

A clear `status` key helps the model understand whether the tool succeeded and
what to do next.

Pattern:

```python
return {
    "status": "success",
    "data_key": value,
    "another_key": another_value,
}
```

Or on error:

```python
return {
    "status": "error",
    "error_message": "Human-readable explanation of what went wrong",
}
```

Why this matters:

* the model can tell success from failure
* the model can decide whether to retry or apologize
* structured output is easier to reason about
* error messages help the assistant respond clearly

## What Makes This Different From Built-In Tools

Built-in tools:

* are imported from ADK
* are maintained by the ADK team
* solve common tasks such as search or code execution

Custom tools:

* are written by you
* are maintained by your team
* solve logic specific to your product or business

## When To Use Custom Tools

Use custom tools when you:

* need logic that is unique to your business
* must connect to proprietary systems
* want full control over validation and error handling
* need a small, focused operation the model can call reliably

Good examples:

* `calculate_shipping`
* `lookup_order_status`
* `validate_loyalty_points`
* `issue_refund`

## When Not To Use Custom Tools

Do not write a custom tool when a built-in tool or MCP server already solves
the problem well.

Prefer built-in tools for:

* Google Search
* code execution

Prefer MCP when:

* an external server already exists for the capability
* you want a standardized connector to a shared tool ecosystem

When the agent already has several tools, move to
`references/agent-orchestration.md` so the instructions can coordinate them
properly.

## Source Note

This reference is based on ADK's function tools documentation and the project
guidance for choosing the right integration approach.
