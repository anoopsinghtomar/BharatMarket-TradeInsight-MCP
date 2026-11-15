def choose_tool(discovered_tools: list[dict], required_capability: str) -> dict | None:
    """Conservative placeholder: selection must be reviewed against descriptions/schemas."""
    matches = [
        tool for tool in discovered_tools
        if required_capability.lower() in (tool.get("description") or "").lower()
    ]
    return matches[0] if len(matches) == 1 else None
