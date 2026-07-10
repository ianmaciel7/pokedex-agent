# The need for an agent in a sandbox

Use this reference when the conversation is about why enterprise agents need a
secure sandbox, what the managed runtime provides, and how resource access is
scoped.

## Core idea

A real business task often needs more than a chat model. It may require code
execution, data access, network access, and credentials. That makes the
runtime a security boundary, not just an implementation detail.

The Managed Agents API responds by starting with a secure, isolated sandbox
and then adding agent logic on top.

## Why the sandbox matters

The enterprise questions are:

* where does the data sit?
* what can the agent touch?
* what can it reach on the network?

The sandbox gives the platform a place to enforce those boundaries before the
agent runs.

## What the sandbox provides

The module lists these core systems and controls:

* persistent file system
* Bash terminal
* preloaded toolchain
* network isolation
* extensible integrations
* MCP credential scoping
* data scoping for Cloud Storage and Skill Registry mounts
* project access

## Control boundary

The diagram in the lesson highlights three parts:

* project IAM controls who can call the agent;
* the platform service account reads data on the agent's behalf with a
  downscoped token;
* the sandbox runs without credentials of its own and with no egress until it
  is opened.

## Lifecycle settings

The lesson also calls out sandbox parameters such as:

* sandbox environment
* sandbox time to live (TTL)
* agent configuration persistence
* agent collaboration through a shared `env_id`

## What to remember

Choose the managed runtime when you want:

* a secure, isolated foundation;
* platform-managed boundaries around data and credentials;
* less infrastructure to build and operate yourself.

Choose a developer framework when you want more direct control of the runtime
and deployment target.
