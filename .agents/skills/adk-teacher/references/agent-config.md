# Agent Generation Config

Use this reference when tuning `LlmAgent` generation behavior with
`generate_content_config`.

## What It Is

This config controls how the model generates text.

Use it when the default behavior is not the right fit for the task.

## What It Changes

* `temperature` controls randomness.
* Lower `temperature` gives more stable answers.
* Higher `temperature` gives more variety.
* `max_output_tokens` limits response length.
* `top_p` and `top_k` affect sampling.
* Safety settings help control risky output.

## When To Use It

Use `generate_content_config` when the agent is correct, but the output needs
different style, length, or variability.

Typical cases:

* reduce cost by using a smaller model setup
* make answers more factual and less creative
* enforce safety or compliance constraints

## Mental Model

Think of it as the agent's generation profile.

In Python, these settings usually live inside
`types.GenerateContentConfig`.

## Source Note

This reference is based on:

https://adk.dev/agents/llm-agents/#fine-tuning-llm-generation-generate_content_config
