def research_snapshot(symbol: str, metrics: dict, coverage: float) -> dict:
    return {
        "symbol": symbol.upper(),
        "metrics": metrics,
        "data_coverage": coverage,
        "research_type": "historical market behaviour; not fundamental quality",
    }
