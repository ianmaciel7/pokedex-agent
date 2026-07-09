# google-agents-cli-observability Reference

Use this reference when inspecting logs, traces, metrics, status, or runtime
errors for a deployed Pokédex ADK agent.

## Command Discovery

Do not assume the exact observability command. Start by discovering available
commands:

```sh
google-agents-cli-observability --help
uv run google-agents-cli-observability --help
google-agents-cli-deploy --help
uv run google-agents-cli-deploy --help
```

If the observability CLI is unavailable, inspect the deploy CLI for list,
describe, status, logs, or trace commands. If neither CLI is available, report
the missing tooling and ask whether to install it.

## Required Inputs

Resolve these before cloud log or trace calls:

- Google Cloud project ID.
- Region.
- Runtime target, such as Agent Runtime, Agent Engine, Cloud Run, or GKE.
- Deployment name, resource ID, endpoint, service name, or trace ID.
- Time window for logs.
- Severity or error filter, when provided.

Use `gcloud config get-value project` and `gcloud config get-value compute/region`
as hints only. Ask for missing values that cannot be safely inferred.

## Inspection Flow

1. Confirm the deployment identity with list or describe commands.
2. Inspect status or health fields before reading logs.
3. Read recent error and warning logs for the requested time window.
4. Follow trace IDs or dashboard links emitted by the CLI.
5. Report concise findings with timestamps and resource IDs.

## Typical Command Intent

Use the installed CLI's help output to choose exact syntax. Intended operations
may include:

```sh
google-agents-cli-observability logs DEPLOYMENT_ID --project PROJECT_ID --region REGION
google-agents-cli-observability traces DEPLOYMENT_ID --project PROJECT_ID --region REGION
google-agents-cli-deploy agent-engine logs DEPLOYMENT_ID --project PROJECT_ID --region REGION
```

If the CLI exposes Cloud Logging commands, use the filters it suggests rather
than inventing resource labels.

## Reporting

Report:

- Target project, region, runtime, and deployment ID.
- Time window inspected.
- Error count or notable severity levels.
- Short redacted log snippets only when useful.
- Trace IDs and dashboard links when available.
- Whether the evidence points to auth, permissions, dependency, model provider,
  runtime startup, or application logic.

## Failure Handling

- Authentication failure: verify with `gcloud auth list`; use
  `gcloud-auth-verification` if available.
- Permission failure: identify the missing IAM permission from the error.
- Missing resource: re-check project, region, runtime target, and deployment ID.
- Oversized logs: narrow by time window, severity, trace ID, or deployment ID.
