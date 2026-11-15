from datetime import datetime, timedelta, timezone
from nse_research.data.validators.freshness import is_stale


def test_stale_timestamp():
    now = datetime.now(timezone.utc)
    assert is_stale(now - timedelta(minutes=20), now=now, max_age_minutes=10) is True


def test_missing_timestamp_is_unknown():
    assert is_stale(None) is None
