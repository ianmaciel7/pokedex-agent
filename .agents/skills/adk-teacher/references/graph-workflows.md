# Graph workflows

Use this reference when the conversation is about graph-based routing and
multi-node execution in ADK.

## Core idea

Graph workflows combine agents and deterministic nodes into an execution graph.
That makes branching, routing, and structured control flow explicit.

## Why it matters

Graph workflows help when you need:

* predictable execution paths;
* branching logic;
* deterministic steps mixed with agent reasoning;
* clearer inspection of complex flows.

## Main themes

* Graph routes: choose the next node based on conditions.
* Data handling: pass and transform structured data between nodes.
* Human input: pause for review or approval where needed.
* Dynamic workflows: change the path programmatically at runtime.

## When to use it

Use graph workflows when simple delegation is not enough and the structure of
the process matters.

## Good pattern

1. Identify the decision points.
2. Separate deterministic steps from reasoning steps.
3. Make the data flow explicit.
4. Add human review only where it adds value.

## Source note

Official URLs:
- https://adk.dev/graphs/
- https://adk.dev/graphs/routes/
- https://adk.dev/graphs/data-handling/
- https://adk.dev/graphs/human-input/
- https://adk.dev/graphs/dynamic/
