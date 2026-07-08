# google-agents-cli-deploy Reference

Use this reference when a user asks to create, update, inspect, observe, or
delete a cloud deployment for the Pokédex ADK agent.

## Command Discovery

Do not assume the exact CLI surface. Start each session by discovering the
installed command:

```sh
google-agents-cli-deploy --help
google-agents-cli-deploy agent-engine --help
google-agents-cli-deploy agent-runtime --help
```

If the binary is unavailable but the project uses `uv`, try:

```sh
uv run google-agents-cli-deploy --help
```

If neither works, stop and tell the user the CLI is missing. Ask whether to add
or install the package that provides `google-agents-cli-deploy`.

## Required Inputs

Resolve these before create, update, or delete:

- Google Cloud project ID
- Region
- Target runtime, defaulting to Agent Runtime / Agent Engine
- Deployment name or resource ID
- ADK app/package path, usually `pokedex_agent`
- Entry point, usually `pokedex_agent.agent:root_agent` or the CLI's ADK default
- Service account, only when the user or environment provides one
- Environment variables and secrets, without printing secret values

Use `gcloud config get-value project` and `gcloud config get-value compute/region`
as hints only. Ask for missing values that cannot be safely inferred.

## Create Or Update

Use the CLI's help output to choose the exact subcommand. The intended operation
should look like one of these shapes:

```sh
google-agents-cli-deploy agent-engine deploy \
  --project PROJECT_ID \
  --region REGION \
  --app pokedex_agent \
  --display-name DEPLOYMENT_NAME
```

```sh
google-agents-cli-deploy agent-runtime deploy \
  --project PROJECT_ID \
  --region REGION \
  --app pokedex_agent \
  --display-name DEPLOYMENT_NAME
```

If the installed CLI uses different nouns, map the workflow to the discovered
commands. Keep Agent Runtime / Agent Engine as the default target unless the user
chooses another supported target.

After a successful deploy, capture the deployment ID, endpoint, project, region,
runtime target, and console URL from command output.

## Inspect, Logs, And Observability

Prefer CLI-native list, describe, logs, and status commands. Typical intent:

```sh
google-agents-cli-deploy agent-engine list --project PROJECT_ID --region REGION
google-agents-cli-deploy agent-engine describe DEPLOYMENT_ID --project PROJECT_ID --region REGION
google-agents-cli-deploy agent-engine logs DEPLOYMENT_ID --project PROJECT_ID --region REGION
```

If the CLI exposes observability dashboards or trace links, report those links.
If it does not, report the available status fields and any Cloud Logging command
suggested by the CLI.

## Delete

Before deletion, identify exactly one deployment. If the user gave a fuzzy name,
list matching deployments and ask for the exact deployment ID.

Use the CLI's delete/remove command discovered from help. Typical intent:

```sh
google-agents-cli-deploy agent-engine delete DEPLOYMENT_ID \
  --project PROJECT_ID \
  --region REGION
```

After delete, run list or describe again. Report whether the deployment is gone,
marked deleting, or still present.

## Failure Handling

- Authentication failure: verify with `gcloud auth list`; use the
  `gcloud-auth-verification` skill if available.
- Permission failure: identify the missing IAM permission or API from the error;
  do not ask the user to re-login when the active account is already present.
- Missing API enablement: report the service named by the CLI error and ask
  before enabling APIs.
- Missing dependency: ask whether to add the CLI dependency to the project or
  install it in the current environment.
- Ambiguous command syntax: show the relevant `--help` result summary and use
  the command form documented by the installed CLI.
