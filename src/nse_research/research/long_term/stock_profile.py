def build_stock_profile(symbol: str, history_available: bool, missing_metrics: list[str]) -> dict:
    return {
        "symbol": symbol.upper(),
        "historical_data_available": history_available,
        "fundamental_metrics": "unavailable unless explicitly exposed by a verified approved source",
        "missing_metrics": missing_metrics,
    }
