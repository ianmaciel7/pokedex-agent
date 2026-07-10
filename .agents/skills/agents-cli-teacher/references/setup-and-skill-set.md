# Setting up agents-cli and the ADK skill set

Use this reference when the conversation is about installing agents-cli,
verifying the local setup, loading the right skills, or keeping the toolchain
current.

## Core idea

agents-cli is the local toolchain for ADK development. It covers scaffolding,
dependency management, linting, playground testing, evaluation, and deployment.
Its setup flow also installs the skill files that keep a coding agent aligned
with the ADK 2.0 API surface.

## Prerequisites

The local setup depends on:

* Python 3.11 or newer
* `uv`
* Node.js 18 or newer

Deployment-related phases also need the Google Cloud SDK and Terraform, but
those are not required for the local development loop.

## Authentication

There are two common authentication paths:

* Google Cloud credentials via ADC or `gcloud`
* `GOOGLE_API_KEY` from Google AI Studio

For the ADK workflows in this course, Google Cloud credentials are the
preferred path because they support Vertex AI, Cloud Run, and Vertex AI
Session Service.

## Setup flow

The recommended bootstrap command is:

```bash
uvx google-agents-cli setup
```

This command:

1. verifies credentials,
2. installs `agents-cli`,
3. downloads the skill files into `~/.agents/skills/`.

If `uvx` is unavailable, install `uv` first and rerun the setup.

## Verification

After setup, verify the install with:

```bash
agents-cli --version
agents-cli info
```

Use `agents-cli info` to confirm the skills were detected locally.

## Seven skills

The standard skill set described in the lesson includes:

* `google-agents-cli-workflow`
* `google-agents-cli-adk-code`
* `google-agents-cli-scaffold`
* `google-agents-cli-eval`
* `google-agents-cli-deploy`
* `google-agents-cli-publish`
* `google-agents-cli-observability`

## Session-start pattern

At the start of an ADK build session, confirm the skills and credentials first,
then name the API surface you want the agent to use.

Example prompt:

```text
Install the agents-cli toolchain and its ADK skills so you can help me build
an ADK agent. Run "uvx google-agents-cli setup", then confirm with
"agents-cli info" and tell me which skills are now available.
```

When moving into a specific phase, explicitly load the relevant skills so the
agent does not drift to an older API or a different workflow.

## Updating

The toolchain and the ADK API evolve together. When they change, update both:

* `agents-cli update` to refresh the installed skills
* `uv tool upgrade google-agents-cli` to upgrade the binary

For teams, pin the `google-agents-cli` version and document the exact ADK
version used by the project.
