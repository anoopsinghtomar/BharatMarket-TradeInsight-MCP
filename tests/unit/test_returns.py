import pandas as pd
import pytest
from nse_research.analytics.technical.returns import period_return, daily_returns


def test_period_return():
    assert period_return(pd.Series([100, 110, 120]), 2) == pytest.approx(0.2)


def test_period_return_insufficient_data():
    assert period_return(pd.Series([100, 110]), 2) is None


def test_daily_returns():
    result = daily_returns(pd.Series([100, 110]))
    assert pd.isna(result.iloc[0])
    assert result.iloc[1] == pytest.approx(0.1)
