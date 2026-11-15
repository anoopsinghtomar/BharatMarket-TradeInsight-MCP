import pandas as pd


def annualized_volatility(close: pd.Series, periods_per_year: int = 252) -> float | None:
    returns = close.astype(float).pct_change().dropna()
    if len(returns) < 2:
        return None
    return float(returns.std(ddof=1) * periods_per_year**0.5)
