# Module introduction: Managed Agents on Agent Platform

Use this reference when the conversation is about the core tradeoff between
code-first and infrastructure-first agent development on Gemini Enterprise
Agent Platform.

## Main idea

Enterprises often want to secure the runtime before adding agent logic. This
module explains the infrastructure-first model used by the Managed Agents API:

* define a secure, isolated runtime first;
* add the agent's logic on top;
* keep data and credentials contained;
* separate agent definition from agent execution.

## Two approaches

### Code-first

With a developer framework such as ADK, you usually start from code and decide
how to host and secure infrastructure later.

### Infrastructure-first

With the Managed Agents API, you start with a secure runtime and then layer the
agent behavior on top.

## Why it matters

This approach is useful for enterprises that need to answer:

* where does the data go?
* what can the agent reach?
* how is the environment secured before launch?

It reduces security drift and helps keep the deployment auditable and
controlled.

## Platform model

The module highlights the split between:

* the control plane, which defines agents; and
* the data plane, which runs them.

It also introduces the idea that the platform manages the runtime while you
provide the custom logic.

## What an agent is built from

The module describes an agent as a combination of:

* a definition;
* a sandboxed environment;
* mounted data;
* tools;
* skills.

## What the learner should leave with

After this module, the reader should be able to:

* choose between developer frameworks and infrastructure-first frameworks;
* secure infrastructure, identity, and network access around an agent;
* configure the Agents API across control and data planes;
* distinguish platform-managed infrastructure from custom logic.
