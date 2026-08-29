import pytest
from durations import parse


def test_readme_forms():
    assert parse("90s") == 90
    assert parse("45m") == 2700
    assert parse("1h30m") == 5400
    assert parse("2h05m") == 7500
    assert parse("2d") == 172800
    assert parse("1:30") == 5400
    assert parse("0:45") == 2700


def test_rejects():
    with pytest.raises(ValueError):
        parse("soon")
