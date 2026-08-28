from pay.money import to_cents


def test_basic():
    assert to_cents("12.34") == 1234


def test_no_fraction():
    assert to_cents("7") == 700


def test_single_decimal():
    assert to_cents("0.5") == 50
