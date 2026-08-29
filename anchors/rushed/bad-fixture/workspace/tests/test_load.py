import pytest

from importer import load


def test_loads_rows(tmp_path):
    p = tmp_path / "ok.csv"
    p.write_text("date,site,count\n2026-08-20,alpha,3\n")
    rows = load(str(p))
    assert rows[0].site == "alpha" and rows[0].count == 3


def test_rejects_bad_date():
    with pytest.raises(ValueError) as e:
        load("fixtures/sample.csv")
    assert "line 5" in str(e.value)
