# Agent Tools

Use this reference when introducing built-in ADK tools.

## What It Is

Built-in tools are ready-made ADK capabilities. Use them for common tasks
instead of writing your own implementation.

## Why It Matters

Building common tools yourself adds API setup, error handling, maintenance, and
extra runtime work.

Built-in tools save time and stay more consistent.

## Main Examples

This lesson focuses on:

1. Google Search for current information.
2. Code execution for math and computation.

## Google Search

Use Google Search when the agent needs recent or grounded web information.

Example:

```python
from google.adk.agents import LlmAgent
from google.adk.tools import google_search

search_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="search_agent",
    instruction="Use web search to answer current questions.",
    tools=[google_search],
)
```

Key points:

* import the tool instead of building it
* use Gemini 2.0 or newer
* show rendered search content in the app layer when the tool returns it

## Code Execution

Use code execution when the agent needs exact math, data processing, or
validation.

Example:

```python
from google.adk.agents import LlmAgent
from google.adk.code_executors import BuiltInCodeExecutor

code_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="code_agent",
    instruction="Use code execution for accurate calculations.",
    code_executor=BuiltInCodeExecutor(),
)
```

Key points:

* this uses `code_executor`, not `tools`
* it is better for precision than plain model arithmetic
* it is useful for step-by-step calculations and transformations

## Session State

Built-in tools can use session state for context-aware behavior.

Common uses:

* store user preferences
* reuse earlier results
* personalize search or calculations

## When To Use Built-In Tools

Use built-in tools for common capabilities like search and computation.

Use custom tools when the logic is specific to your business.

## Source Note

This reference is based on the ADK built-in tools docs:

https://google.github.io/adk-docs/tools/built-in-tools/

## Source note

Official URLs:
- https://adk.dev/tools/limitations/
