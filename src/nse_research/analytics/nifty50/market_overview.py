from typing import Any


def summarize_index_record(record: dict[str, Any]) -> dict[str, Any]:
    """Normalize only fields present in a validated source record."""
    fields = ("open", "high", "low", "close", "previous_close", "change_percent", "volume")
    return {key: record[key] for key in fields if key in record}
