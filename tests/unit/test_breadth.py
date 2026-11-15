from nse_research.analytics.nifty50.breadth import advance_decline_ratio, breadth_label


def test_advance_decline_ratio():
    assert advance_decline_ratio(60, 40) == 1.5


def test_zero_declines_is_unavailable_ratio():
    assert advance_decline_ratio(60, 0) is None


def test_breadth_label():
    assert breadth_label(60, 40, 5) == "positive"
