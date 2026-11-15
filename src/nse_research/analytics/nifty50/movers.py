import pandas as pd


def rank_movers(frame: pd.DataFrame, change_column: str, limit: int = 10):
    if limit <= 0:
        raise ValueError("limit must be positive")
    if change_column not in frame:
        raise KeyError(change_column)
    clean = frame.dropna(subset=[change_column])
    return clean.nlargest(limit, change_column), clean.nsmallest(limit, change_column)
