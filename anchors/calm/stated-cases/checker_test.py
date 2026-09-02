import pytest
from durations import parse


def test_reported_bug_fixed():
    assert parse("1h30m") == 5400
    assert parse("2h05m") == 7500


def test_no_regressions():
    assert parse("90s") == 90
    assert parse("45m") == 2700


def test_rejects():
    with pytest.raises(ValueError):
        parse("soon")
