# Run and operate the agent

Use this reference when the conversation is about running an assembled agent
on the data plane and preparing it for production.

## Main idea

This module moves from definition to execution.

The agent already exists on the control plane. Now you run it on the data
plane, where the platform executes runs, streams reasoning, returns typed
results, and carries state across turns.

## Data plane role

The data plane is the part of the platform that actually executes the runs.

An interaction is not the same as the durable agent definition. It is an
ephemeral run that uses the assembled configuration.

## What happens during a run

The lesson describes runs as:

* happening in the background;
* unfolding as a streamed reason-act loop;
* producing reliable typed results;
* reusing state across turns.

## Blueprint idea

One assembled agent can represent a family of reusable blueprints.

That means the same definition can support many interactions and can be
reshaped over time as the codebase evolves.

## Production concerns

The module also emphasizes security and operational practices for production:

* secure the agent for deployment;
* apply the operational model needed for reliable runtime behavior;
* understand how the agent will be operated after assembly.

## What the learner should leave with

After this module, the reader should be able to:

* perform synchronous background runs;
* create interactions with reliable typed results;
* persist state across turns;
* understand how one codebase can produce multiple reusable blueprints;
* apply production security and operational practices.
