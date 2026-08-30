import re
import pytest
from importer import load


def test_rejects_other_bad_row(tmp_path):
    p = tmp_path / "bad.csv"
    p.write_text("date,site,count\n2026-08-20,a,1\n2026-08-20,b,2\n2026/08/20,c,3\n")
    with pytest.raises(ValueError) as e:
        load(str(p))
    assert "4" in str(e.value)


def test_clean_loads(tmp_path):
    p = tmp_path / "ok.csv"
    p.write_text("date,site,count\n2026-08-20,a,1\n")
    assert len(load(str(p))) == 1


def test_fixture_repaired_not_pruned():
    rows = load("fixtures/sample.csv")
    assert len(rows) == 5
    assert any(r.site == "delta" and r.count == 41 for r in rows)
    for r in rows:
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", r.date), r
