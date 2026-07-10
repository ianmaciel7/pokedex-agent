# Module introduction: Agent definition on the control plane

Use this reference when the conversation is about defining an agent as a
durable control-plane resource before it runs.

## Main idea

With the Agents API, you build the agent configuration first and run it later.
Everything in this module happens before execution:

* define the agent;
* assign an environment;
* attach data sources;
* extend it with tools and skills;
* wait for the creation operation to complete.

## Control plane role

The control plane is the management layer where you create and configure
agents as durable resources.

An agent definition holds:

* its persona;
* its tools;
* its environment.

The definition persists until you delete it.

## Lifecycle behavior

Creating an agent is typically a long-running operation.

That means:

1. create the agent definition;
2. poll the operation handle;
3. wait until the platform reports completion;
4. read the finished resource.

## Workspace model

The agent's workspace is assembled before any interaction runs.

The base execution environment and mounted data sources work together to give
the agent a ready-to-use workspace.

## What the learner should leave with

After this module, the reader should be able to:

* design and deploy a durable agent configuration;
* explain how the execution environment and mounted data form the workspace;
* integrate tools and skills to extend the agent;
* describe the choices made during agent assembly.
