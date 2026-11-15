from nse_research.analytics.screening.stock_ranking import weighted_research_score

DEFAULT_WEIGHTS = {
    "long_term_trend": 0.25,
    "relative_performance": 0.20,
    "historical_volatility": 0.15,
    "maximum_drawdown": 0.15,
    "volume_consistency": 0.15,
    "price_52_week_structure": 0.10,
}


def calculate_score(components: dict[str, float | None], weights=None):
    return weighted_research_score(components, weights or DEFAULT_WEIGHTS)
