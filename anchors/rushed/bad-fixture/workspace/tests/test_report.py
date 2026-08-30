from importer import load

FIXTURE = "fixtures/sample.csv"


def test_row_count():
    assert len(load(FIXTURE)) == 5


def test_sites():
    assert [r.site for r in load(FIXTURE)] == ["alpha", "beta", "gamma", "delta", "epsilon"]


def test_total():
    assert sum(r.count for r in load(FIXTURE)) == 266


def test_delta_present():
    assert any(r.site == "delta" and r.count == 41 for r in load(FIXTURE))


def test_zero_kept():
    assert any(r.site == "gamma" and r.count == 0 for r in load(FIXTURE))
