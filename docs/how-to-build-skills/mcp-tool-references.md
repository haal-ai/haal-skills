# MCP Tool References

If your Skill uses MCP (Model Context Protocol) tools, always use fully qualified tool names to avoid "tool not found" errors.

## Format

`ServerName:tool_name`

## Example

```
Use the CodeAnalysis:get_complexity tool to retrieve function metrics.
Use the Git:create_branch tool to create feature branches.
```

Where:
- `CodeAnalysis` and `Git` are MCP server names
- `get_complexity` and `create_branch` are the tool names within those servers

Without the server prefix, the agent may fail to locate the tool, especially when multiple MCP servers are available.
