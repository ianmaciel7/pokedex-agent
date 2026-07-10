# State across turns and blueprints

Use this reference when the conversation is about reusing conversation state,
reusing a workspace, or composing many blueprints from one agent definition.

## Main idea

By default, each interaction starts fresh.

To continue work, you pass back two independent handles on the next run:

* the previous interaction identifier, to continue the conversation;
* the environment identifier, to reuse the same workspace.

## Conversation scope

The previous interaction identifier brings back the dialogue so far, including
earlier outputs and discovered results.

That is the handle for the interaction scope.

## Environment scope

The environment identifier re-attaches the agent to the same sandbox.

That preserves:

* mounted data;
* mounted skills;
* intermediate files.

The two handles are independent, so you can keep one without the other.

## Multi-turn pitfall

Do not create a fresh environment for the second turn unless you truly want a
new workspace.

Reusing the captured environment identifier avoids losing prior work and avoids
re-provisioning cost.

## Blueprint composition

Once you assemble one agent, you can think of it as a family of reusable
blueprints.

The stable parts are:

* the identifier;
* the base agent;
* the description;
* the instruction.

The parts that vary are:

* mounted sources;
* offered tools.

That means you can create blueprints such as:

* an agent grounded on stored data;
* an agent driven by a single packaged skill;
* an agent integrated with a live external system;
* an agent that mounts a library of skills;
* a composite that combines all of them.

## What to remember

There is no special composite setting.
Composition is just a longer sources list and a longer tools list.

The design question is simple: what does the agent need to reach?
