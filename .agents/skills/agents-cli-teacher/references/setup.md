# Setup

Use this reference when the conversation is about installing agents-cli, local
setup, the skill set, and keeping the toolchain current.

## Prerequisites

* Python 3.11 or newer
* `uv`
* Node.js 18 or newer

Deployment phases also need the Google Cloud SDK and Terraform.

## Authentication

Two common paths work:

* Google Cloud credentials via ADC or `gcloud`
* `GOOGLE_API_KEY` from Google AI Studio

For the course workflow, Google Cloud credentials are the preferred path
because they support Vertex AI, Cloud Run, and Session Service.

## Setup flow

```bash
uvx google-agents-cli setup
```

That command verifies credentials, installs `agents-cli`, and downloads the
skill files into `~/.agents/skills/`.

## Verify the install

```bash
agents-cli --version
agents-cli info
```

## Skills available in the local setup

The standard skill set described in the course includes:

* `google-agents-cli-workflow`
* `google-agents-cli-adk-code`
* `google-agents-cli-scaffold`
* `google-agents-cli-eval`
* `google-agents-cli-deploy`
* `google-agents-cli-publish`
* `google-agents-cli-observability`

## Load skills by phase

Load only the skills relevant to the current phase, then reload them when you
move into a different phase. That keeps context focused and avoids drift.

## Update the toolchain

* `agents-cli update` refreshes the installed skills.
* `uv tool upgrade google-agents-cli` upgrades the binary.

Pin versions for team use when you need reproducibility.

## Troubleshooting

If a skill is missing or the setup looks stale, rerun:

```bash
uvx google-agents-cli setup
```

If you need a pinned version for a team, use:

```bash
uv tool install google-agents-cli==<version>
```

If you start with `GOOGLE_API_KEY` and later add a Google Cloud project, rerun
`uvx google-agents-cli setup` to pick up the new credentials.

Common fixes:

* rerun setup after a bad or partial install
* confirm `uv` is on `PATH`
* confirm Node.js is 18 or newer
* recheck `GOOGLE_API_KEY` or ADC if auth fails
* use the pinned install command when a team needs a fixed release

## Session-start pattern

Start each build session by confirming the toolchain and the loaded skills,
then explicitly naming the API surface you want the agent to use.

This keeps Antigravity or another coding agent from drifting to a different
API or an older workflow.

Example session start:

```text
Install the agents-cli toolchain and its ADK skills so you can help me build
an ADK agent. Run "uvx google-agents-cli setup", then confirm with
"agents-cli info" and tell me which skills are now available.
```
