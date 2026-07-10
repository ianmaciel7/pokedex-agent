# Agent Session

Use this reference when explaining session state, `output_key`, `{var}`
templating, and state namespaces in ADK.

## What It Covers

Session data has three related parts:

* `session.state`: stored values your code can read and write.
* `output_key`: automatic storage of the agent's final text response.
* `{var}` templating: instruction text resolved from session state before the
  LLM sees it.

It also covers state namespaces:

* `temp:` for one turn.
* no prefix for one session.
* `user:` for one user across sessions.
* `app:` for the whole app.

## Core Idea

Conversation history helps the LLM remember what was said.
Session state helps your code store and check exact values.

Use session state when you need programmatic control, not just model context.

## `session.state`

`session.state` is a dictionary-like store.

Use it for data such as:

* user names
* task progress
* preferences
* routing flags

Example:

```python
session.state["user_name"] = "Alex"
session.state["conversation_topic"] = "refunds"
```

Read values safely with `.get()`:

```python
name = session.state.get("user_name", "Guest")
```

## `output_key`

Use `output_key` when you want the final agent response saved automatically.

Example:

```python
from google.adk.agents import LlmAgent

agent = LlmAgent(
    model="gemini-2.5-flash",
    instruction="Extraia o tópico principal. Retorne SOMENTE o tópico.",
    output_key="topic",
)
```

If the agent responds with `quantum computing`, ADK stores:

```python
session.state["topic"] = "quantum computing"
```

## `{var}` Templating

Use `{var}` placeholders in instructions to inject state values.

Example:

```python
instruction="Olá, {user_name}, como posso te ajudar hoje?"
```

If `session.state["user_name"] = "Alex"`, the LLM receives:

```text
Olá, Alex, como posso te ajudar hoje?
```

Use `{key?}` when the value may be missing:

```python
instruction="Olá, {user_name?Guest}"
```

## State Namespaces

Namespaces control how long values persist.

| Namespace | Prefix | Scope |
| --- | --- | --- |
| Temporary | `temp:` | Current turn only |
| Session | none | Current session |
| User | `user:` | One user across sessions |
| App | `app:` | Whole application |

Examples:

```python
session.state["temp:current_step"] = "validating"
session.state["conversation_topic"] = "refunds"
session.state["user:theme"] = "dark"
session.state["app:api_url"] = "https://api.example.com"
```

## Quick Rule

Choose the smallest scope that still fits the data:

* use `temp:` for one turn
* use no prefix for one session
* use `user:` for one user across sessions
* use `app:` for shared app-wide values

## Mental Model

Ask:

* Does this value belong to the current turn?
* Does it belong to the current conversation?
* Does it belong to one user across conversations?
* Does it belong to the whole app?

## Source Note

This reference is based on ADK documentation for session state, templating,
and namespaces.

Useful docs:

* https://google.github.io/adk-docs/sessions/state.md#accessing-session-state-in-agent-instructions
* https://google.github.io/adk-docs/sessions/state.md#organizing-state-with-prefixes-scope-matters
