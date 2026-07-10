# Build with the Managed Agents API on Gemini Enterprise Agent Platform

Use this reference when the conversation is about the managed agent runtime on
Gemini Enterprise Agent Platform, enterprise governance, or the control-plane
and data-plane model.

## Course focus

This course teaches how to build and run enterprise agents on the Managed
Agents API. The main ideas are:

* a business task may require an agent rather than a chat model;
* the platform separates a control plane from a data plane;
* an agent is assembled from a definition, sandboxed environment, mounted
  data, tools, and skills;
* runtime behavior includes background interactions, a streamed reason-act
  loop, typed results, and state that persists across turns.

## Hands-on goal

The course includes a lab where you build and harden a retail merchandising
agent for Cymbal Retail from an empty project to a production-shaped
deployment.

The intended outcome is to be able to design, build, and operate a managed
agent of your own.

## Security and operations

The course emphasizes:

* reducing security configuration drift;
* avoiding unmanaged agent sprawl;
* delivering auditable, secure, zero-trust AI environments;
* shortening deployment time;
* applying production security and operational practices.

## Intended audience

The course is aimed at:

* Security Teams
* Cloud Architects
* AI Platform Engineers

It assumes familiarity with:

* networking primitives such as VPC and DNS;
* identity and access management concepts.

## What to remember

When using this material, keep the distinction clear between:

* the control plane, which defines agents; and
* the data plane, which runs them.

Also remember that this course is about managed enterprise agents, not the
local ADK development loop.
