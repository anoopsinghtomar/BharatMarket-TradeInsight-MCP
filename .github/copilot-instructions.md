# Project: NSE AI Research

## Objective
Build an evidence-based Indian stock market research application using official hosted NSE MCP as the exclusive market-data source in the initial version.

## Technology
- Python 3.11+
- Official MCP Python SDK; remote Streamable HTTP
- Streamlit, Pandas, NumPy, Plotly
- SQLite initially; Pytest and Ruff

## Official NSE endpoints
- Bhavcopy: https://mcp.nseindia.in/bhavcopy/cm/mcp
- CM Market: https://mcp.nseindia.in/cmmkt/mcp

## Non-negotiable data rules
- Do not use yfinance, Yahoo Finance, Google Finance, scraping or unofficial market-data APIs.
- Never fabricate or estimate prices.
- Never silently substitute a provider.
- Mark unavailable fields and stale information explicitly.
- Preserve market date, retrieval timestamp, source server, discovered tool and input parameters.
- The LLM interprets validated data; it is never the source of market facts.

## MCP implementation
- Use the official MCP Python SDK and Streamable HTTP.
- Discover tools dynamically and inspect their input schemas.
- Never hardcode assumed tool names or parameters.
- Handle connection errors, timeouts and malformed responses.
- Document verified tool capabilities in docs/mcp_integration.md.
- Do not claim integration success based on mocks.

## Analytics and research
- Keep analytics deterministic and implemented in Python.
- Include formula, observation period and data coverage.
- Missing observations must not be assigned zero or favourable values.
- Market performance is not fundamental business quality.
- Do not invent revenue, profitability, debt, ROE, ROCE, cash flow or valuation data.

## Engineering
- Modular monolith; separate UI, application, data access, analytics and research.
- Type hints, small functions, structured logging and tests.
- Synthetic fixtures are for unit tests only and must never be presented as actual NSE data.
- Never commit secrets, local databases or private generated reports.
- Implement and test incrementally; do not generate the entire application in one step.

## Initial priority
Connect to both remote NSE MCP endpoints, discover actual tools and schemas, test real responses, and document findings before implementing market analytics.
