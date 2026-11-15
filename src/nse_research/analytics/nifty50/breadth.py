def advance_decline_ratio(advances: int, declines: int) -> float | None:
    if advances < 0 or declines < 0:
        raise ValueError("breadth counts cannot be negative")
    if declines == 0:
        return None
    return advances / declines


def breadth_label(advances: int, declines: int, unchanged: int = 0) -> str:
    if min(advances, declines, unchanged) < 0:
        raise ValueError("breadth counts cannot be negative")
    if advances > declines:
        return "positive"
    if declines > advances:
        return "negative"
    return "balanced"
