# MCP Integration

Use this reference when an ADK agent needs external tools through the Model
Context Protocol (MCP).

## What It Is

MCP is a standard way to connect agents to external tools and data sources.

Think of it as a shared connector layer:

* one protocol
* many compatible servers
* many compatible clients

## Why It Matters

Without MCP, each integration needs custom glue code.

With MCP:

* the tool owner can maintain the server
* the agent can reuse the server through one interface
* the integration stays more portable

## Main Pattern

This reference focuses on the common pattern where the ADK agent acts as an
MCP client.

Flow:

1. The MCP server exposes tools.
2. ADK connects with `McpToolset`.
3. The tools are discovered automatically.
4. The agent calls them like normal ADK tools.

## `McpToolset`

`McpToolset` is the bridge between ADK and MCP.

Use it inside the agent's `tools` list.

Example:

```python
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

agent = LlmAgent(
    model="gemini-2.5-flash",
    name="my_agent",
    instruction="Use the available tools to help users.",
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args=["-y", "@some/mcp-server"],
                ),
            ),
        )
    ],
)
```

## Connection Types

### `StdioConnectionParams`

Use this for a local server process.

Good for:

* development
* testing
* local setups

### `SseConnectionParams`

Use this for a remote server over HTTP.

Good for:

* production
* hosted servers
* cloud deployments

## Tool Filtering

Use `tool_filter` to expose only the tools the agent actually needs.

This helps with:

* security
* simplicity
* lower tool noise

Example:

```python
McpToolset(
    connection_params=StdioConnectionParams(...),
    tool_filter=["list_directory", "read_file"],
)
```

## Which Tool Style To Use

* Use built-in ADK tools for common features like search or code execution.
* Use MCP when a server already exists for the capability.
* Use custom function tools for business-specific logic.

## Common MCP Server Areas

Common server categories include:

* filesystem access
* GitHub
* Slack
* databases
* Notion
* Google Drive

## Source Note

This reference is based on ADK MCP docs and the MCP specification:

* https://google.github.io/adk-docs/mcp/
* https://google.github.io/adk-docs/tools/mcp-tools/
* https://modelcontextprotocol.io/

## Source note

Official URLs:
- https://adk.dev/integrations/
- https://google.github.io/adk-docs/mcp/
- https://google.github.io/adk-docs/tools/mcp-tools/
