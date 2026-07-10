# Managed Agents

Use this reference when the conversation is about Gemini Enterprise Agent
Platform, the managed runtime, or the control-plane/data-plane split.

## Overview

Enterprises often want to secure the runtime before adding agent logic.
Managed Agents starts with infrastructure and then layers logic on top.

### Two approaches

* Code-first: start from code, secure and host later.
* Infrastructure-first: start with a secure runtime, then add behavior.

### Why it matters

This model helps enterprises answer:

* where does the data go?
* what can the agent reach?
* how is the environment secured before launch?

## Sandbox

The managed runtime begins with a secure, isolated sandbox.

The environment is provisioned lazily, at first interaction, which keeps agent
definition cheap.

The lesson also describes the sandbox as a standard isolated Linux container.

### What the sandbox provides

* persistent file system
* Bash terminal
* preloaded toolchain
* network isolation
* extensible integrations
* MCP credential scoping
* data scoping for Cloud Storage and Skill Registry mounts
* project access

### Security boundary

* Project IAM controls who can call the agent.
* The platform service account reads data on your behalf with a downscoped
  token.
* The sandbox has no credentials of its own and no egress until opened.

### Operational settings

* sandbox environment
* sandbox time to live (TTL)
* agent configuration persistence
* agent collaboration through a shared `env_id`

### Execution characteristics

* the sandbox runs code and reads or writes files
* the network allowlist is closed by default
* fine-grained host allowlisting is not yet available

The sandbox provides a place to enforce boundaries before the agent runs.

## Interaction model

The platform splits work into two APIs:

* Agents API for creating and configuring the agent
* Interactions API for running the agent at runtime

### Control plane

The Agents API defines an agent once as a durable cloud resource.

Example:

```python
client.agents.create(id="cymbal-merch-analyst", base_agent=..., system_instruction=...)
```

### Data plane

The Interactions API runs the agent.
Each interaction is ephemeral and drives the reason-act loop to completion.

Example:

```python
client.interactions.create(agent="cymbal-merch-analyst", input="Umbrella sales dropped 18%...")
```

### Long-running operations

Agent creation returns an operation handle first.
Poll until it is done, then read the finished resource.

Over REST, you poll the operation yourself. In SDK flows, the client may handle
that polling for you.

Always check for errors, because an operation can report done and still carry
an error instead of an agent.

## Agent definition

The definition is small and durable.

### Core fields

* `id` names the resource and cannot be changed later
* `base_agent` selects the foundation agent
* `description` documents the agent
* `system_instruction` defines persona and rules
* `tools` lists what the agent may use
* `base_environment` bounds the runtime

### Workspace model

The base environment and mounted data sources create the workspace before any
interaction runs.

Mounted files appear as ordinary files inside the sandbox.

### Mounting data

Mount Cloud Storage data into the sandbox so the agent can read it as normal
files.

The platform reads private buckets with the per-project service account, so the
bucket must grant that account read access.

The source object is a small three-field mount descriptor:

```json
{"type":"gcs","source":"gs://my-bucket","target":"/.agent/data"}
```

## Configuration, environment, and data

Use `base_environment` to define the runtime.

### Environment pieces

* `type` selects the environment kind
* `sources` defines what to mount
* `network` controls the allowlist

### Example environment

```json
{
  "type": "remote",
  "sources": [],
  "network": {"allowlist": [{"domain": "*"}]}
}
```

### Production note

The current release only accepts a wildcard allowlist entry.
Fine-grained host allowlisting is not yet available.

## Tools and skills

Tools are actions.
Skills are reusable packaged logic and content.

### Tool types

* built-in tools
* external systems through Model Context Protocol
* local functions in your application

### Skills

A skill is a directory anchored by `SKILL.md` with optional scripts,
references, and assets.

To publish a skill, you package the directory, encode it, and create it in the
Skill Registry.

The lesson describes the registry as a regional surface. Agents and
interactions live in the global location, but skills live in a specific region.

Before mounting a skill, you first need to find it.

### Registry

Publish skills into the Skill Registry, then mount them into the agent.
Skill creation is a long-running operation.

### Versioning

Pin versions in production so behavior does not change silently.

During development, you can track the latest version.

## Run and operate

Once the agent is assembled, run it on the data plane.

### What runs

* background execution
* streamed reason-act loop
* reliable typed results
* state across turns

### What to remember

An assembled agent can become a family of reusable blueprints.
The stable parts are the identifier, base agent, description, and instruction.
The variable parts are mounted sources and offered tools.

This is why the design question becomes: what does the agent need to reach?

## Execute and results

Agent runs are asynchronous and must be marked as background runs.

### Background runs

Capture the run identifier and store the interaction when you want to continue
the conversation later.

```python
run = client.interactions.create(
    agent=AGENT, input=task, background=True, store=True
)
run_id = run.id
```

If you forget the background flag, the platform rejects the call.

Store the interaction if you want to retrieve it later or continue it as a
multi-turn conversation.

### Reason-act loop

The loop is a sequence of:

* model-output
* function-call
* function-result

The final answer is the last non-empty model-output step.

If the very last step is empty, scan backward until you find the last
non-empty model-output step.

The loop repeats as think, act, observe until the task is resolved.

### Streaming

Streamed runs emit created, start, delta, stop, and completed events.

You can handle all event types with a single consumer.

The stream starts with a created event, then emits start, delta, and stop
events for each step, and ends with a completed event.

The platform continues to run on the server even if the connection drops.

### Typed results

Pass a response schema when you want machine-readable output.

```python
client.interactions.create(
    agent=AGENT,
    input=task,
    background=True,
    store=True,
    response_format=DeclineReport,
)
```

### Usage

Capture input tokens, output tokens, and thought tokens from the completed
stream event.

## State across turns and blueprints

Reuse two handles to continue work:

* previous interaction identifier for the conversation
* environment identifier for the workspace

### Scope

* interaction scope keeps the dialogue and earlier results
* environment scope keeps mounted data, mounted skills, and intermediate files

### Three nested scopes

* iteration scope
* interaction scope
* environment scope

### Pitfall

Do not create a new environment by default on the second turn.
Reuse the captured environment identifier instead.

The two handles are independent, so you can keep one without the other.

## Security and hardening

The security model keeps personal credentials out of the sandbox.

### Layers

* Identity and Access Management
* Platform Service Account
* Isolated Sandbox

### IAM roles

* `aiplatform.user` to execute interactions
* `aiplatform.admin` to create, update, or delete agents

### Containment

* no ambient credentials
* downscoped, per-source tokens
* closed egress by default
* scoped tool credentials
* explicit data paths

When you attach an MCP connection with an authentication header, the platform
sends that header only to the endpoint you declared.

### Hardening

Use a narrow allowlist in production and update the environment with a PATCH
when you need to harden an existing agent.

Example update pattern:

```http
PATCH .../agents/cymbal-merch-analyst?update_mask=base_environment
```

### Operational discipline

* rely on the result accessor that raises on failure
* log usage as telemetry
* keep the parsed step stream as an execution log

That execution log answers why the agent decided something because it shows
the exact tool results before the final answer.
