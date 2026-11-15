import pandas as pd
from nse_research.analytics.technical.moving_averages import moving_average
from nse_research.analytics.technical.drawdown import maximum_drawdown
from nse_research.analytics.technical.volatility import annualized_volatility


def test_moving_average_requires_full_window():
    result = moving_average(pd.Series([1, 2, 3]), 2)
    assert pd.isna(result.iloc[0])
    assert result.iloc[1] == 1.5


def test_maximum_drawdown():
    assert maximum_drawdown(pd.Series([100, 120, 90, 110])) == -0.25


def test_volatility_requires_two_returns():
    assert annualized_volatility(pd.Series([100, 101])) is None
