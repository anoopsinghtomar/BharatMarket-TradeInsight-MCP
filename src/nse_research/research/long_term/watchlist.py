from datetime import datetime


def watchlist_entry(symbol: str, notes: str = "") -> dict:
    return {
        "symbol": symbol.upper(),
        "notes": notes,
        "added_at": datetime.now().astimezone().isoformat(),
    }
