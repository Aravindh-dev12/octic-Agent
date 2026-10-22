# Octic AI Agent — MCP Compatibility Integration

This optional integration exposes supported Octic agent capabilities through the Model Context Protocol (MCP), for clients such as Cursor and Claude Desktop. It is not needed for the standalone Octic runtime or HTTP API.

## Install

From the repository root:

```bash
python -m pip install -e "src/octic_ai_agent[compat,mcp]"
```

Set the provider credentials required by your selected model.

## Quick start

```bash
octic-ai-agent mcp serve --transport stdio
octic-ai-agent mcp list-tools
```

For help:

```bash
octic-ai-agent mcp --help
```

These extended commands are dispatched through the explicit compatibility integration. The underlying separately packaged MCP host still uses its legacy distribution and internal module identifiers for compatibility; those are not the public Octic product name.

## Layers

| Layer | Role |
|---|---|
| MCP client | Connects an agent to a remote MCP server |
| Light server | Exposes selected tools over an MCP transport |
| Optional compatibility host | Provides the extended host/capability registry integration |

Keep provider secrets out of checked-in configuration. Review each tool's permissions before exposing it to an MCP client.
