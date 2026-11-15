def positive_relative_performance(stock_return: float | None, index_return: float | None) -> bool | None:
    if stock_return is None or index_return is None:
        return None
    return stock_return > index_return
