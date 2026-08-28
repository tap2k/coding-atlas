from export import export_legacy


def test_legacy(tmp_path):
    p = tmp_path / "l.txt"
    assert export_legacy(str(p)) == 2
    assert p.read_text().splitlines()[0] == "20260827|ALPHA|000012"
