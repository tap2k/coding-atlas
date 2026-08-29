import pytest

from durations import parse


def test_seconds():
    assert parse("90s") == 90


def test_minutes():
    assert parse("45m") == 2700



def test_rejects_garbage():
    with pytest.raises(ValueError):
        parse("soon")
