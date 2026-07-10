# Defining the agent: configuration, environment, and data

Use this reference when the conversation is about the durable agent
definition on the control plane, especially its configuration, environment,
and mounted data.

## Main idea

The Agents API lets you define an agent before it runs. The definition is a
small set of fields that describe the agent's persona, runtime, and mounted
workspace.

Everything here happens before execution:

* set the agent identity;
* choose the base agent;
* define the instruction and tools;
* attach the execution environment;
* mount the data the agent will read.

## Agent definition fields

The module highlights these core fields:

* `id` names the durable resource and cannot be changed later;
* `base_agent` selects the foundation agent;
* `description` documents the agent;
* `system_instruction` defines persona and rules;
* `tools` lists what the agent may use;
* `base_environment` bounds the runtime.

## Long-running creation

Creating an agent follows the long-running operation pattern.

The platform returns an operation handle first, then you poll until it is done
and read the created agent. The SDK hides this loop, but over REST you handle
it yourself.

Always check for errors even when the operation reports done.

## Execution environment

The `base_environment` gives the agent a workspace to run in.

The lesson describes a remote environment as a managed, isolated Linux
container that is provisioned lazily on the first interaction.

The environment also includes:

* a sources list for mounts;
* a network allowlist.

## Mounting data

To give the agent data, mount a Cloud Storage source into the sandbox.

The lesson describes the source as having three fields:

* `type`
* `source`
* `target`

Mounted files appear as normal files inside the sandbox and can be read by the
agent with file-system access and code execution.

## Access note

The sandbox does not read private buckets using the caller's credentials.
Instead, the platform reads them with the per-project service account.

That means the bucket must grant the service account read access, or the mount
will fail at runtime.

## What the learner should leave with

After this module, the reader should be able to:

* design a durable agent configuration;
* explain the relationship between execution environment and mounted data;
* integrate tools and skills into the definition;
* recognize the long-running creation workflow;
* avoid mount failures caused by missing service-account access.
