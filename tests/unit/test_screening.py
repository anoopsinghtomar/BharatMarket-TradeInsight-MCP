from nse_research.analytics.screening.stock_ranking import weighted_research_score


def test_missing_score_is_excluded_and_coverage_reported():
    score, coverage = weighted_research_score(
        {"trend": 80, "risk": None},
        {"trend": 0.6, "risk": 0.4},
    )
    assert score == 80
    assert coverage == 0.6


def test_no_available_components():
    score, coverage = weighted_research_score(
        {"trend": None}, {"trend": 1.0}
    )
    assert score is None
    assert coverage == 0
