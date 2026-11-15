# Architecture

The application is a modular monolith with six logical layers:

1. Presentation: Streamlit pages and reusable UI components.
2. Application/research: coordinates pre-market, long-term and assistant workflows.
3. Data access: official remote NSE MCP clients, discovery, invocation and provenance.
4. Validation: schema, type, date, numerical and freshness checks.
5. Analytics: deterministic Pandas/NumPy calculations.
6. Storage: SQLite initially, subject to NSE storage/retention terms.

The UI must never call MCP directly. It should call application services. Analytics must not know about Streamlit or LLM providers.
