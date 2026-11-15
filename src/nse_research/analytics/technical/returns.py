import pandas as pd


def period_return(close: pd.Series, periods: int = 1) -> float | None:
    if periods <= 0:
        raise ValueError("periods must be positive")
    values = close.dropna().astype(float)
    if len(values) <= periods or values.iloc[-periods - 1] == 0:
        return None
    return float(values.iloc[-1] / values.iloc[-periods - 1] - 1.0)


def daily_returns(close: pd.Series) -> pd.Series:
    return close.astype(float).pct_change()
