# Interaction with the agent in a sandbox

Use this reference when the conversation is about how the platform splits
definition from execution, and what the control plane and data plane each do.

## Two APIs

The module separates interaction into two APIs:

* the Agents API for creating and configuring the agent;
* the Interactions API for running the agent at runtime.

## Agents API

The Agents API is the control plane.

You use it to define an agent once as a durable cloud resource with a name.
The definition holds the agent's persona, tools, and environment, and it
persists until you delete it.

## Interactions API

The Interactions API is the data plane.

You use it to run the agent. Each interaction references the agent by name,
binds an environment, and drives the reason-act loop to completion.

An interaction is ephemeral and exists for one run.

## Long-running operations

Creating an agent returns a long-running operation, not the finished agent
immediately.

Treat that as the platform doing background work:

1. poll the operation handle;
2. wait until it reports done;
3. read the finished agent.

## What the platform runs for you

The platform handles the runtime pieces around the reason-act loop, including:

* orchestration;
* secure sandboxing;
* credential management;
* network control.

## What you provide

You provide the intent and configuration:

* system instruction;
* allowed tools;
* environment bounds.

The platform then runs the loop, manages state, dispatches tool calls, and
provisions and tears down the sandbox.

## Key distinction

Use the control plane to define the agent once.
Use the data plane to run it many times.

That separation is the core operational model behind the Managed Agents API.
