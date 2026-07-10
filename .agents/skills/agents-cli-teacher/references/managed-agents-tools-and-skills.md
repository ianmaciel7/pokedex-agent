# Extend agent capabilities with tools and skills

Use this reference when the conversation is about giving an agent external
actions or reusable procedures.

## Core distinction

Tools are actions the agent can choose to take while it runs.
Skills are mounted directories of files and scripts that extend the agent's
logic.

## Tool types

The lesson distinguishes three kinds of tools:

* built-in tools
* external systems exposed through Model Context Protocol (MCP)
* local functions in your application

### Local functions

Local functions stay in your codebase.

The SDK passes the function to the model, your process runs it, and the result
returns on the next turn.

Use local functions when the logic must stay in code rather than in the
sandbox or a remote service.

## Tool selection

Tools are listed on the agent definition as entries in a tools list.

You choose which tools to offer, and the model decides which ones to use, with
what arguments, and in what order.

## Skills

A skill is a directory anchored by a required `SKILL.md` file and optional
scripts, references, and assets.

Skills are different from tools:

* tools are actions;
* skills are reusable packaged logic and content.

## Skill Registry

To publish a skill, you package the directory, encode it, and create it in the
Skill Registry.

The lesson describes the registry as a regional surface. Agents and
interactions live in the global location, but skills live in a specific
region.

Skill creation is a long-running operation, so you poll it to completion just
like agent creation.

## Mounting skills

Before mounting a skill, you first need to find it.

Once mounted, the skill becomes part of the assembled agent alongside the
sandbox, mounted data, and tools.

## Versioning

In production, pin a specific skill version so updates do not silently change
agent behavior.

During development, you can track the latest version.

## What the learner should leave with

After this module, the reader should be able to:

* distinguish tools from skills;
* identify the three tool kinds;
* explain how MCP fits into external integrations;
* describe how skills are packaged and published;
* choose when to pin or float a skill version.
