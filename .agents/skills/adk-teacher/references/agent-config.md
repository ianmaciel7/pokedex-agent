# Agent Generation Config

Use this reference when tuning ADK `LlmAgent` generation behavior with
`generate_content_config`.

## Problems It Solves

`generate_content_config` is useful when the default model behavior is not a
good fit for the task.

Common problems:

* Unnecessary cost from using a larger or more capable model than the task
  needs.
* Inconsistent or overly creative answers when the task needs factual or
  exact output.
* Missing safety or compliance controls when the agent is used in a public or
  regulated setting.

## Good Mental Model

Think of this as the agent's generation profile:

* Lower `temperature` reduces randomness and makes output more deterministic.
* Higher `temperature` increases variation and creativity.
* `max_output_tokens` caps how long the response can be.
* `top_p` and `top_k` shape the token sampling strategy.
* Safety settings help align output with policy, risk, or compliance needs.
* In Python, these are often represented as `types.SafetySetting` entries
  inside `types.GenerateContentConfig`.

## When To Use It

Use `generate_content_config` when the agent is otherwise correct, but the
response style, length, or variability needs tuning.

## Source Note

This reference is based on the ADK documentation section:

https://adk.dev/agents/llm-agents/#fine-tuning-llm-generation-generate_content_config
