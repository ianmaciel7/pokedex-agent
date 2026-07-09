# Google Agents CLI Reference

Use this reference when working with a Google Agents CLI command. Treat
official documentation and installed `--help` output as the first source of
truth for command behavior.

## Command Discovery

Do not assume the exact CLI surface. Start by discovering the installed
command family and the relevant subcommands from `--help`.

If the binary is unavailable, continue with the local project's existing
structure when possible. Ask before adding new dependencies.

## Required Inputs

Resolve these before taking action:

- Target package, app path, or resource
- Intended task or phase
- Expected runtime behavior
- Required credentials, without printing secret values

## Execution Flow

Use this workflow when executing the task:

### Primary Actions

1. Identify the exact target of the change or command.
2. Confirm the intended command family from installed help output.
3. Resolve the minimum required inputs before proceeding.
4. Use the narrowest command or workflow that satisfies the request.
5. Keep the next action explicit and easy to validate.

### Secondary Actions

1. Re-run focused commands when clarification is needed.
2. Prefer small, verifiable steps over broad speculative changes.
3. Distinguish command issues, environment issues, and product issues.
4. Capture the relevant identifiers, outputs, or state changes.

## Validation

Run the relevant `--help` command and any focused verification step that matches
the task.

If runtime behavior changed and credentials are available, run the smallest
relevant verification command for the current target.

## Reporting

Report:

- Commands used
- Files changed or resources affected
- Checks passed, failed, or skipped
- Any assumptions about credentials, command availability, or target identity

## Failure Handling

- Missing command: ask whether to add the dependency to the project.
- Authentication failure: verify credentials without printing secret values.
- Permission failure: identify the missing permission or API from the error.
- Ambiguous CLI syntax: summarize the relevant help output and use the installed form.

## Safety

- Do not print or commit API keys, tokens, credentials, or local `.env` values.
- Prefer installed CLI help output over remembered syntax.
