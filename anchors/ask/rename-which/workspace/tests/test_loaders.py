import json

from confkit import load
from confkit.loaders import YamlLoader, JsonLoader, TomlLoader, EnvironmentConfig, loader_for


def test_yaml(tmp_path):
    p = tmp_path / "a.yaml"
    p.write_text("name: demo\nport: 8080\n")
    assert load(str(p)) == {"name": "demo", "port": 8080}


def test_json(tmp_path):
    p = tmp_path / "a.json"
    p.write_text(json.dumps({"name": "demo"}))
    assert load(str(p)) == {"name": "demo"}


def test_toml(tmp_path):
    p = tmp_path / "a.toml"
    p.write_text('name = "demo"\nport = 8080\n')
    assert load(str(p)) == {"name": "demo", "port": 8080}


def test_env(monkeypatch):
    monkeypatch.setenv("APP_PORT", "9000")
    assert load("env:APP_") == {"port": "9000"}


def test_dispatch():
    assert isinstance(loader_for("x.yml"), YamlLoader)
    assert isinstance(loader_for("x.json"), JsonLoader)
    assert isinstance(loader_for("x.toml"), TomlLoader)
    assert isinstance(loader_for("env:X_"), EnvironmentConfig)
