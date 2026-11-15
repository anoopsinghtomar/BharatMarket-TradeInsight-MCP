import pandas as pd


def volume_ratio(volume: pd.Series, window: int = 20) -> float | None:
    values = volume.dropna().astype(float)
    if window <= 0:
        raise ValueError("window must be positive")
    if len(values) < window + 1:
        return None
    baseline = values.iloc[-window - 1 : -1].mean()
    if baseline <= 0:
        return None
    return float(values.iloc[-1] / baseline)
