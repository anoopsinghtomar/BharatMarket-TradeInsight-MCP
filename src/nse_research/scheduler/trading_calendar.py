from datetime import date


def is_configured_trading_day(day: date, holidays: set[date], special_sessions: set[date]) -> bool:
    if day in special_sessions:
        return True
    if day.weekday() >= 5 or day in holidays:
        return False
    return True
