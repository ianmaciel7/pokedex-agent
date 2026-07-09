# Structured Agent Data

Use this reference when working with ADK `LlmAgent` structured data settings.
It covers `input_schema`, `output_schema`, and `output_key`.

## What These Fields Do

Use these fields when the agent needs structured input, structured output, or
state handoff between steps.

* `input_schema`: defines the expected input shape. When set, the user message
  content passed to the agent must be a JSON string that matches the schema.
* `output_schema`: defines the desired output shape. When set, the agent's
  final response should conform to the schema.
* `output_key`: defines the session state key that receives the agent's final
  response text.

## Good Mental Model

Think of the fields this way:

* `input_schema` validates what comes in.
* `output_schema` constrains what comes out.
* `output_key` stores the final output for later reuse.

## Important Distinction

These are not general-purpose Python or TypeScript types. They are schema-based
controls for structured agent I/O.

## Source Note

This reference is based on the ADK documentation section:

https://adk.dev/agents/llm-agents/#structuring-data-input_schema-output_schema-output_key
