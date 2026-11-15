# NSE MCP integration

## Official endpoints

- Bhavcopy: `https://mcp.nseindia.in/bhavcopy/cm/mcp`
- CM Market: `https://mcp.nseindia.in/cmmkt/mcp`

## Connection model

The application uses the official MCP Python SDK and remote Streamable HTTP. It does not launch a local NSE MCP server.

## Discovery-first requirement

Run:

```bash
python scripts/discover_mcp_tools.py
```

For every discovered tool, review and document:

- Server name and endpoint
- Exact tool name and description
- Complete input schema, required and optional parameters
- Output content shape and error shape
- Supported date ranges and symbol conventions
- Example response captured from an actual call (sanitize as appropriate)
- Retrieval timestamp and observed data freshness
- Research use cases and limitations

The discovery script writes `docs/mcp_tool_catalogue.json`. Review the output before checking in any catalogue. Tool names and schemas are deliberately not pre-populated in source code.

## Invocation

`NSEMCPClient.call_tool()` first lists the current tool catalogue and refuses to invoke a name that is not exposed. Add domain-specific wrappers only after inspecting the live schema.

## Live integration status

Not yet verified by this scaffold. Run the discovery and connection scripts in an environment with network access. A passing unit test or mocked test is not evidence that the remote service is available.
