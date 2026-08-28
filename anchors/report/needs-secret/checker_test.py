from pay.money import to_cents


def test_bug_fixed():
    assert to_cents("0.5") == 50
    assert to_cents("12.34") == 1234
    assert to_cents("3.05") == 305
