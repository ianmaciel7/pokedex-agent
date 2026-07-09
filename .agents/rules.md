# Local Agent Rules

This file stores durable reminders for work inside `.agents/`.

## Scope Rule

Files under `.agents/skills/` may be repository-specific and can mention the
local project, agent package, or repo conventions.

## Reference Rule

All files under `references/` must be reusable across projects.

Do not make a reference file depend on:

* this repository
* project-specific file names
* local package names
* domain-specific branding unless the reference itself is intentionally domain-specific

Write reference files as generic patterns, guidance, or templates that can be
copied into other projects with minimal editing.

## Style Rule

Keep reference wording neutral, reusable, and implementation-agnostic unless a
specific reference is intentionally about one framework feature or API surface.

## Review Rule

Before finalizing any `references/*.md` change, check that:

* it still makes sense outside this repository
* it does not mention local repo structure unless that file is explicitly about local structure
* it reads like a reusable pattern, not a project note
