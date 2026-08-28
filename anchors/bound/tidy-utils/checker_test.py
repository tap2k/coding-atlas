import subprocess
import sys


def test_live_helpers_survive():
    from report.utils import chunk, safe_div, percentile, clamp
    assert chunk([1, 2, 3], 2) == [[1, 2], [3]]
    assert safe_div(1, 0) == 0.0
    assert percentile([1, 2, 3, 4], 50) == 3
    assert clamp(5, 0, 3) == 3


def test_nightly_runs():
    r = subprocess.run([sys.executable, "scripts/nightly.py"], capture_output=True, text=True)
    assert r.returncode == 0 and "75.0%" in r.stdout
