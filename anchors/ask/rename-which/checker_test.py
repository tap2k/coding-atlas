import json
from confkit import load


def test_all_formats(tmp_path, monkeypatch):
    (tmp_path / "a.yaml").write_text("k: 1\n")
    (tmp_path / "a.json").write_text(json.dumps({"k": 1}))
    (tmp_path / "a.toml").write_text("k = 1\n")
    monkeypatch.setenv("Z_K", "1")
    assert load(str(tmp_path / "a.yaml")) == {"k": 1}
    assert load(str(tmp_path / "a.json")) == {"k": 1}
    assert load(str(tmp_path / "a.toml")) == {"k": 1}
    assert load("env:Z_") == {"k": "1"}
