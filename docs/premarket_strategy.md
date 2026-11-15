# Pre-market strategy

Proposed workflow (Asia/Kolkata):

- 08:45 — establish remote NSE MCP connections
- 08:50 — retrieve latest available completed-session data
- 08:53 — validate and calculate indicators
- 08:56 — generate evidence-grounded interpretation
- 09:00 — publish report
- 09:20 — optional post-opening update

These are target execution times, not guarantees of NSE service availability. At 09:00 the report must use the latest completed session and must not claim a complete pre-open snapshot unless verified.

The scheduler must use a maintained NSE holiday/special-session calendar. A simple weekday cron trigger alone is insufficient for production.
