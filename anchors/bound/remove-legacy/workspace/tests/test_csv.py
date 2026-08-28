from export import export_csv


def test_csv(tmp_path):
    p = tmp_path / "r.csv"
    assert export_csv(str(p)) == 2
    assert p.read_text().splitlines()[0] == "date,site,count"
