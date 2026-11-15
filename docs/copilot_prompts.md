# GitHub Copilot Agent prompts

Use these prompts sequentially. Read `README.md` and `.github/copilot-instructions.md` first.

## Prompt 1 — Foundation and MCP
Build the project foundation and remote NSE MCP client using the official Python SDK and Streamable HTTP. Discover both servers' actual tools and input schemas. Do not assume tool names, use unofficial data, or implement the Streamlit dashboard yet. Add tests and document live integration evidence.

## Prompt 2 — Tool catalogue
Inspect both official NSE MCP servers. Document every actual tool name, description, input schema, required/optional parameters, response structure, sample response, errors and use cases in `docs/mcp_integration.md`. Create a reviewed machine-readable catalogue. Do not invent anything.

## Prompt 3 — Nifty 50 analytics
Use only verified tools and validated source fields. Implement index overview, historical performance, breadth, movers, available sectors, moving averages, returns and volume analysis. Add unit tests and document unsupported metrics.

## Prompt 4 — Pre-market reporting
Build a 09:00 IST report using the latest completed session, configurable trading calendar, scheduler, Markdown builder, storage and logs. Handle weekends, holidays, special sessions and missing data. Never imply a full pre-open snapshot without evidence.

## Prompt 5 — Long-term research
Implement historical returns, moving averages, relative performance, volatility, drawdown, volume, 52-week analysis, configurable score, comparison and watchlists. Do not call market performance fundamental business quality or invent financial ratios.

## Prompt 6 — AI assistant
Implement intent identification, evidence context, discovered-tool routing, validated retrieval, Python calculations, provider adapter, response validation and research history. Every numerical market claim must be traceable.

## Prompt 7 — Streamlit dashboard
Implement the six dashboard pages using existing application services. Keep MCP logic out of UI pages. Use Plotly, loading states, errors, provenance, freshness and missing-data warnings.
