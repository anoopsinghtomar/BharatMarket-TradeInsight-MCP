import pandas as pd


def drawdown_series(close: pd.Series) -> pd.Series:
    values = close.astype(float)
    peaks = values.cummax()
    return values / peaks - 1.0


def maximum_drawdown(close: pd.Series) -> float | None:
    values = close.dropna().astype(float)
    if values.empty or (values <= 0).any():
        return None
    return float((values / values.cummax() - 1.0).min())
