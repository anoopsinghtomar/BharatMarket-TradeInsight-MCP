def bullish_ma_alignment(ma_50: float | None, ma_200: float | None) -> bool | None:
    if ma_50 is None or ma_200 is None:
        return None
    return ma_50 > ma_200
