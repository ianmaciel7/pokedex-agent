# Agent Session

Use this reference when explaining session state, `output_key`, `{var}`
templating, and namespaces.

## What It Is

Session data has three main parts:

* `session.state` for values your code can read and write
* `output_key` for saving the final response
* `{var}` templating for inserting state into instructions

## Core Idea

Conversation history helps the model remember the chat.
Session state helps your code store exact values.

Use session state when you need programmatic control.

## `session.state`

Use `session.state` for things like:

* user names
* preferences
* progress
* routing flags

Example:

```python
session.state["user_name"] = "Alex"
session.state["conversation_topic"] = "refunds"
```

## `output_key`

Use `output_key` when you want the final response saved automatically.

Example:

```python
from google.adk.agents import LlmAgent

agent = LlmAgent(
    model="gemini-2.5-flash",
    instruction="Return only the main topic.",
    output_key="topic",
)
```

If the agent returns `quantum computing`, ADK stores that value in
`session.state["topic"]`.

## `{var}` Templating

Use `{var}` to inject state into instructions.

Example:

```python
instruction="Hello, {user_name}, how can I help?"
```

Use `{key?fallback}` when a value may be missing.

## State Namespaces

Namespaces define how long values last:

| Namespace | Prefix | Scope |
| --- | --- | --- |
| Temporary | `temp:` | One turn |
| Session | none | One session |
| User | `user:` | One user across sessions |
| App | `app:` | Whole app |

## Quick Rule

Use the smallest scope that still fits the data:

* `temp:` for one turn
* no prefix for one session
* `user:` for one user across sessions
* `app:` for shared app values

## Source Note

This reference is based on ADK docs for session state and namespaces:

* https://google.github.io/adk-docs/sessions/state.md#accessing-session-state-in-agent-instructions
* https://google.github.io/adk-docs/sessions/state.md#organizing-state-with-prefixes-scope-matters
