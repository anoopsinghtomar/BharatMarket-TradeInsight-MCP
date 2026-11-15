from datetime import date, datetime


def build_report(
    report_date: date,
    session_date: str | None,
    sections: dict[str, str],
    warnings: list[str] | None = None,
) -> str:
    lines = [
        f"# NSE Pre-Market Research — {report_date.isoformat()}",
        "",
        f"- Session date: {session_date or 'Unavailable'}",
        f"- Generated at: {datetime.now().astimezone().isoformat()}",
        "- Data source: Official NSE MCP only",
        "",
    ]
    for heading, body in sections.items():
        lines.extend([f"## {heading}", "", body or "Unavailable — no verified data supplied.", ""])
    if warnings:
        lines.extend(["## Data limitations", ""])
        lines.extend(f"- {warning}" for warning in warnings)
    return "\n".join(lines)
