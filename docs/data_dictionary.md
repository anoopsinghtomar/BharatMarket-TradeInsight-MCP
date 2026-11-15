# Data dictionary

| Field | Meaning | Rule |
|---|---|---|
| market_date | Session date attached to the source record | Preserve source value; do not infer silently |
| retrieved_at | Application retrieval timestamp | Store timezone-aware timestamp |
| source_server | NSE MCP server identifier | Required provenance |
| tool_name | Exact discovered MCP tool | Required provenance |
| arguments | Parameters passed to the tool | Preserve for reproducibility |
| validation_status | validated / partial / rejected | Derived by validation layer |
| warnings | Missing/stale/invalid data observations | Display to user |
| calculation_formula | Formula used for derived metric | Store with metric |
| calculation_period | Lookback/window used | Store with metric |

Market date and retrieval timestamp are separate concepts.
