from nse_research.data.validators.market_data import validate_ohlcv_records


def test_valid_ohlc_record():
    valid, warnings = validate_ohlcv_records(
        [{"open": 10, "high": 12, "low": 9, "close": 11}]
    )
    assert len(valid) == 1
    assert warnings == []


def test_invalid_record_is_rejected():
    valid, warnings = validate_ohlcv_records(
        [{"open": 10, "high": 8, "low": 9, "close": 11}]
    )
    assert valid == []
    assert warnings
