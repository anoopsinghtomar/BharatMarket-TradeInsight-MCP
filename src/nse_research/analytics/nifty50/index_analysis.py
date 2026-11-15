import pandas as pd
from nse_research.analytics.technical.returns import period_return


def index_performance(close: pd.Series) -> dict[str, float | None]:
    return {
        "daily_return": period_return(close, 1),
        "weekly_return": period_return(close, 5),
        "monthly_return": period_return(close, 21),
    }
