"""Market-data-only filters. This module does not assess fundamental business quality."""


def above_long_term_average(price: float | None, moving_average_200: float | None) -> bool | None:
    if price is None or moving_average_200 is None:
        return None
    return price > moving_average_200
