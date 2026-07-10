# Custom Tools

Use this reference when the agent needs business-specific logic.

## What It Is

A custom tool is usually a Python function that ADK exposes to the agent.

When you add the function to `tools`, ADK wraps it as a `FunctionTool`.

## Why It Matters

Built-in tools do not know your business rules, data, or workflows.

Use custom tools for things like:

* shipping rules
* inventory lookup
* refund checks
* loyalty points
* internal scheduling
* order status checks

## How It Works

1. Write a Python function.
2. Add it to the agent's `tools` list.
3. ADK makes it available to the model.
4. The model decides when to call it.
5. The function returns a result.

Example:

```python
from google.adk.agents import LlmAgent


def calculate_shipping_cost(weight_kg: float, country: str) -> dict:
    """Calculate shipping cost for the business."""
    rates = {"usa": 10, "canada": 12, "uk": 15}
    country_key = country.lower()
    if country_key not in rates:
        return {"status": "error", "error_message": f"We do not ship to {country}."}

    cost = weight_kg * rates[country_key]
    return {"status": "success", "cost_usd": round(cost, 2), "country": country}


shipping_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="shipping_agent",
    instruction="Help users with shipping questions.",
    tools=[calculate_shipping_cost],
)
```

## Writing Good Tools

Use clear verb-noun names:

* `get_shipping_cost`
* `calculate_loyalty_points`
* `search_available_flights`

Avoid vague names:

* `process`
* `do_stuff`
* `handler`

Use simple, JSON-friendly types:

* `str`
* `int`
* `float`
* `bool`
* `list`
* `dict`

Prefer required parameters when possible.

## Return Format

Return a dictionary with a clear `status` key.

Good:

```python
return {
    "status": "success",
    "data_key": value,
}
```

Error:

```python
return {
    "status": "error",
    "error_message": "Human-readable explanation",
}
```

## When To Use It

Use custom tools when:

* the logic is unique to your business
* you must connect to proprietary systems
* you want full control over validation and error handling

## When Not To Use It

Do not write a custom tool when a built-in tool or MCP server already solves
the problem well.

## Source Note

This reference is based on ADK docs for function tools and tool choice.

## Source note

Official URLs:
- https://adk.dev/tools-custom/
