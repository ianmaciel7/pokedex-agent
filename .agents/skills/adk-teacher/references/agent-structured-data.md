# Structured Agent Data

Use this reference when working with `input_schema`, `output_schema`, and
`output_key`.

## What It Is

Use these fields when the agent needs structured input, structured output, or
saved output text.

* `input_schema` defines the expected input shape.
* `output_schema` defines the expected output shape.
* `output_key` stores the final response in session state.

## Simple Model

Think of it like this:

* `input_schema` checks what comes in.
* `output_schema` controls what comes out.
* `output_key` saves the final text for later use.

## Important Note

These are schema controls, not general-purpose Python or TypeScript types.

## Source Note

This reference is based on the ADK docs for structured input and output:

https://adk.dev/agents/llm-agents/#structuring-data-input_schema-output_schema-output_key
