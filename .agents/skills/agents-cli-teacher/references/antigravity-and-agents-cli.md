# Antigravity and agents-cli in the ADK development workflow

Use this reference when the conversation is about how Antigravity and
agents-cli work together for local ADK 2.0 development.

## Core idea

Antigravity acts as the agentic IDE that writes and edits code from natural
language design.
agents-cli provides lifecycle knowledge, conventions, and ADK guidance so the
generated code stays closer to the correct API surface from the start.

Together, they help you focus on:

* what the agent should do;
* why the behavior exists;
* how to validate the generated structure;
* when to correct the implementation before moving on.

## Roles

### Antigravity

* Converts design prompts into ADK code.
* Helps assemble graphs, LLM nodes, routing rules, and human review steps.
* Is most useful when the goal is to prototype quickly without memorizing the
  full API.

### agents-cli

* Guides the agent lifecycle: scaffold, build, eval, deploy, publish, and
  observe.
* Helps keep the project aligned with ADK structure and conventions.
* Provides the foundation for local commands, evaluation, and production
  readiness.

## Vibecoding

The lesson frames the developer as the architect:

1. Describe the behavior in natural language.
2. Let the tool generate the implementation.
3. Review the resulting structure.
4. Correct any mismatch before continuing.

This works best when the prompt is specific, behavioral, and explicit about
system boundaries.

## Spec-Driven Development

The lesson recommends writing a formal specification before code.

Good specs:

* define routing rules;
* make it clear what should never reach the LLM;
* document success, failure, and edge-case scenarios;
* serve as the single source for regeneration.

## Pattern example

For an expense agent:

* low-value expenses may be approved automatically;
* high-value expenses may require LLM analysis;
* risky or sensitive cases may require human review;
* the threshold logic should live in code, not in the model.

## Review loop

After the tool generates the flow:

1. ask for a step-by-step explanation;
2. compare it with the original intent;
3. correct any differences;
4. only then move to the next step.

## How to use this reference

Use this material when the question involves:

* how Antigravity and agents-cli complement each other;
* how to write better prompts for ADK workflows;
* how to think about SDD for agents;
* how to review generated code before trusting it.
