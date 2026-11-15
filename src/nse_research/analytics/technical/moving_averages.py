import pandas as pd


def moving_average(close: pd.Series, window: int) -> pd.Series:
    if window <= 0:
        raise ValueError("window must be positive")
    return close.astype(float).rolling(window=window, min_periods=window).mean()
