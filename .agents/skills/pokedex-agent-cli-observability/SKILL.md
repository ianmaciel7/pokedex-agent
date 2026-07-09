---
name: pokedex-agent-cli-observability
description: Inspect logs, traces, metrics, runtime status, errors, or observability dashboards for deployed pokedex-agent Google ADK agents with Google Agents CLI or Google Cloud tooling. Use when Codex is asked to observe, monitor, or debug deployed Pokédex agents.
---

# Pokédex Agent CLI Observability

## Original Skill Reference

This is the Pokédex-local adaptation of the original
`google-agents-cli-observability` skill. Keep the generic CLI guidance in
`references/google-agents-cli-observability.md` as the source reference, then
apply the repository-specific rules in this file.

## Overview

Use this skill to inspect deployed ADK agent behavior through logs, traces,
metrics, and runtime status. Drive observability work through
`google-agents-cli-observability`, deployment CLI status/log commands, or Google
Cloud tooling suggested by the installed CLI.

Treat logs, traces, and request payloads as potentially sensitive. Summarize
what matters and avoid exposing secrets.

## Workflow

1. Confirm the observation target: runtime target, project, region, deployment
   name, resource ID, endpoint, or trace ID.
2. Check credentials and configuration before cloud calls:
   - Run `gcloud auth list` when Google Cloud auth is relevant.
   - Prefer explicit project and region values from user input, environment,
     `gcloud config`, or deployment output.
   - Do not invent project IDs, regions, resource IDs, log names, or trace IDs.
3. Discover available observability commands:
   - Try `google-agents-cli-observability --help`.
   - If that fails, try `uv run google-agents-cli-observability --help`.
   - Also inspect `google-agents-cli-deploy --help` or
     `uv run google-agents-cli-deploy --help` for status and logs commands.
4. Prefer CLI-native status, logs, traces, and dashboard links when available.
5. Parse and report timestamps, severity, error messages, trace IDs, deployment
   IDs, and dashboard links.
6. If the CLI points to Cloud Logging or Trace, use exact resource identifiers
   from deployed agent output or user-provided values.

## Safety Rules

- Never print API keys, bearer tokens, cookies, credentials, or local `.env`
  file contents.
- Redact secrets in log snippets before reporting them.
- Do not assume a deployment is broken until authentication, project, region, and
  resource identity are verified.
- If command output is too large, summarize the relevant errors and include the
  time window inspected.

## CLI Guidance

Read `references/google-agents-cli-observability.md` when planning or executing
logs, traces, metrics, status, or runtime debugging work. Use the reference as a
pattern, then prefer installed CLI help output over remembered syntax.
