# Secure and harden for production

Use this reference when the conversation is about the platform's security
model, data containment, and how to harden an agent for production.

## Core security idea

Your personal credentials never enter the sandbox where the agent runs code.

The platform enforces that boundary through three layers:

* Identity and Access Management
* Platform Service Account
* Isolated Sandbox

## Identity and Access Management

Project access is controlled through IAM.

The lesson names two roles:

* `aiplatform.user` for executing interactions;
* `aiplatform.admin` for creating, updating, or deleting agents.

These roles separate who can run an agent from who can modify one.

## Platform service account

When the agent reaches external systems, the platform sends scoped credentials
only to the endpoint you declared.

That containment extends to MCP connections with authentication headers.

## How data stays contained

The security posture relies on several boundaries:

* no ambient credentials in the sandbox;
* downscoped, per-source tokens;
* closed egress by default;
* scoped tool credentials;
* explicit data paths.

Data leaves the sandbox only through paths you explicitly opened.

## Production hardening

Hardening mostly means applying the security model more narrowly for real
deployments.

The lesson recommends replacing the wide-open development allowlist with an
explicit set of domains the agent actually needs.

The current release only accepts a wildcard allowlist entry, so a specific
domain may return `INVALID_ARGUMENT` until finer-grained allowlisting ships.

## Update pattern

Agent environment changes are REST-only.

To harden an existing agent, send a PATCH that resends the `base_environment`
with the narrowed allowlist and the existing sources.

## Operational discipline

Operate defensively:

* rely on the result accessor that raises on failure;
* log the usage block from each run for cost and latency telemetry;
* keep the parsed step stream as an execution log.

That execution log helps answer why the agent decided something, because it
shows the exact tool results it saw before its final answer.

## What the learner should leave with

After this module, the reader should be able to:

* explain the platform's security posture confidently;
* describe how credentials and data stay contained;
* harden an agent for production;
* understand the current allowlist limitation;
* use run telemetry and step logs for diagnostics.
