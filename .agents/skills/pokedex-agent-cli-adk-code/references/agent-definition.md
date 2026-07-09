# Agent Definition Methods

Use this reference when deciding how to define an ADK agent: directly in code
or through an Agent Config file.

## Terminology

Use **Agent Definition Method** as the umbrella term.

There are two main definition methods:

1. **Code-based Agent Definition**
2. **Config-based Agent Definition**, also called **Agent Config**

Avoid calling these “agent types.” They are not different categories of agents. They are different ways to declare and assemble an agent.

## Code-based Agent Definition

A code-based agent is defined directly in application code.

In Python ADK projects, this usually means defining `root_agent` inside `agent.py`.

```python
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    name="root_agent",
    model="gemini-flash-latest",
    description="Tells the current time in a specified city.",
    instruction=(
        "You are a helpful assistant that tells the current time in cities. "
        "Use the get_current_time tool for this purpose."
    ),
    tools=[get_current_time],
)
```

Use this method when the agent needs custom Python logic, complex tool wiring, dynamic construction, conditional setup, or direct integration with the surrounding application code.

### Best for

* Agents that depend on custom functions or classes.
* Agents that need dynamic setup at runtime.
* Agents with complex Python/Java/TypeScript/Go logic.
* Projects where the agent is part of a larger software system.
* Cases where strong IDE support, refactoring, typing, and tests matter.

### Main tradeoff

Code-based definitions are flexible, but they require developers to read and modify source code to understand or change the agent behavior.

## Config-based Agent Definition / Agent Config

An Agent Config defines the agent with a YAML file instead of defining everything directly in code.

A basic config-based agent uses a file like `agent.yaml`.

```yaml
name: assistant_agent
model: gemini-flash-latest
description: A helper agent that can answer users' questions.
instruction: You are an agent to help answer users' various questions.
```

ADK can create this kind of project with:

```bash
adk create path/to/my_app
```

The installed CLI also supports optional model/backend flags:

```bash
adk create path/to/my_app --model gemini-flash-latest --api_key YOUR_KEY
```

Depending on the backend, `--project` and `--region` may also be accepted for
Vertex AI-backed runs.

This typically generates a project containing an agent config file and `.env`.

Use this method when the agent can be described mostly through declarative fields such as `name`, `model`, `description`, `instruction`, `tools`, and `sub_agents`.

### Best for

* Simple or moderately complex agents.
* Agents whose behavior is mostly instruction-driven.
* Teams that want non-developers to review or edit agent behavior.
* Fast prototyping.
* Separating agent behavior from application code.
* Reusable agent definitions that should be easy to scan.

### Main tradeoff

Agent Config is easier to read and change, but it is less flexible than code. When custom behavior becomes complex, the config may still need to reference code-based tools or supporting modules.

### Practical pattern

In a common hybrid setup, a YAML file is used as a prompt/config source while
the actual agent wiring stays in Python. That makes the definition hybrid:

* YAML owns the shared instructions, root prompts, and specialist prompts.
* Python owns agent construction, sub-agent wiring, and runtime behavior.

Use this pattern when you want the instructions to stay easy to scan, but you
still need code for orchestration, dynamic assembly, or tool integration.

## Comparison

| Question                                                          | Prefer code-based | Prefer Agent Config        |
| ----------------------------------------------------------------- | ----------------- | -------------------------- |
| Does the agent need dynamic runtime setup?                        | Yes               | No                         |
| Is the agent mostly instruction + tools?                          | Maybe             | Yes                        |
| Will non-developers review or edit it?                            | Maybe             | Yes                        |
| Does it need complex custom logic?                                | Yes               | Maybe, with external tools |
| Is quick prototyping the goal?                                    | Maybe             | Yes                        |
| Do you need full IDE refactoring and tests around the definition? | Yes               | Maybe                      |
| Do you want behavior separated from implementation code?          | Maybe             | Yes                        |

## Recommended Decision Rule

Start with **Agent Config** when the agent is mostly declarative.

Move to **code-based definition** when the agent needs complex construction, dynamic behavior, advanced tool setup, or deeper integration with application code.

A practical rule:

> If changing the agent mostly means editing instructions, model names, tools, or sub-agent references, use Agent Config.
> If changing the agent means writing control logic, conditional behavior, custom factories, or complex integrations, use code-based definition.

## Hybrid Pattern

The two methods can be combined.

A config-based agent can reference custom tools implemented in code. This gives you readable YAML for the agent definition while keeping fragile or deterministic logic in Python or another supported language.

Example:

```yaml
agent_class: LlmAgent
name: prime_agent
model: gemini-flash-latest
description: Handles checking if numbers are prime.
instruction: |
  You are responsible for checking whether numbers are prime.
  When asked to check primes, call the check_prime tool.
tools:
  - name: ma_llm.check_prime
```

Use this hybrid pattern when the agent’s behavior should stay readable in YAML, but the actual operation needs reliable code.

In practice, this is a good fit when:

* The prompt changes often, but the wiring changes rarely.
* You want non-developers to review the instruction text.
* The agent still needs custom factories, conditional routing, or strict tool
  integration in code.

## Gotchas

* **Do not call them agent types.** Use “definition methods” or “definition styles.”
* **Agent Config is declarative, not magic.** Complex behavior still belongs in code or tools.
* **Keep instructions readable.** If the YAML instruction becomes huge, move detailed background into a separate reference file or simplify the agent design.
* **Use code for deterministic logic.** Do not force the model to perform calculations, validations, or business rules that should be implemented as tools.
* **Treat `description` as routing metadata.** It should clearly explain what the agent does and when it should be used.
* **Prefer one clear default.** Do not present many equal implementation choices unless the agent truly needs to choose.

## Naming Conventions

Recommended names:

* `AgentDefinitionMethod`
* `AgentDefinitionStyle`
* `code_based`
* `config_based`
* `agent_config`

Example enum:

```python
from enum import Enum

class AgentDefinitionMethod(Enum):
    CODE_BASED = "code_based"
    CONFIG_BASED = "config_based"
```

Recommended documentation heading:

```md
## Agent Definition Methods

ADK agents can be defined in two main ways:

1. Code-based agent definition
2. Config-based agent definition, also known as Agent Config
```

## When Writing a Skill

If this reference is used inside an Agent Skill, keep the main `SKILL.md` short and link to this file only when the task requires choosing, explaining, or refactoring an ADK agent definition method.

Example from `SKILL.md`:

```md
For details about code-based vs config-based ADK agents, read:
references/agent-definition-methods.md
```
