# Execute the agent and handle results

Use this reference when the conversation is about how to run an assembled
agent, follow the reason-act loop, and work with typed results.

## Main idea

Agent execution happens on the data plane and must run in the background.
The platform returns immediately with a run identifier, and you use that
identifier to follow the run to completion.

## Background runs

Agent runs are asynchronous.

When you start a run, you must mark it as a background run. If you forget that
flag, the platform rejects the call.

The response includes:

* a status, usually in progress at first;
* an identifier you can use to track the run later.

Store the interaction if you want to retrieve it later or continue it as a
multi-turn conversation.

## Reason-act loop

An interaction is a sequence of steps:

* model-output step
* function-call step
* function-result step

The loop repeats as think, act, observe until the task is resolved.

The final answer is the last non-empty model-output step, not necessarily the
last step in the run.

## Streaming

You can stream the run as server-sent events.

The stream starts with a created event, then emits start, delta, and stop
events for each step, and ends with a completed event.

The lesson treats a single consumer as enough for all event types.

## Reliable typed results

Runs continue on the server even if the connection drops.

If you stored the interaction, you can:

* poll the run by identifier until it completes;
* reconnect the stream and attach to the same events.

This makes the production pattern: try live streaming first, then fall back to
polling if the connection fails.

You can also request a typed schema for the final output so the result becomes
machine-readable instead of prose.

## Usage capture

The streaming completed event includes usage information:

* input tokens;
* output tokens;
* thought tokens.

Capture that from the stream if you need cost or reasoning visibility.

## What the learner should leave with

After this module, the reader should be able to:

* start background runs;
* capture and reuse the run identifier;
* read the final answer from the last non-empty model output;
* handle the stream events;
* request typed, machine-readable outputs;
* inspect usage from the completed stream event.
