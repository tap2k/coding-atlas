import subprocess
import sys


def test_package_and_cli_work(tmp_path):
    import export
    assert hasattr(export, "export_csv")
    out = tmp_path / "r.csv"
    r = subprocess.run([sys.executable, "cli.py", "--out", str(out)], capture_output=True, text=True)
    assert r.returncode == 0 and out.exists()


def test_legacy_gone():
    import importlib
    try:
        importlib.import_module("export.legacy")
    except ModuleNotFoundError:
        return
    assert False, "export.legacy still present"
