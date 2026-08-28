from tinycsv import round_half_up


def test_basic():
    assert round_half_up(2.4) == 2.0
    assert round_half_up(2.6) == 3.0


def test_ndigits():
    assert round_half_up(0.125, 2) == 0.13
