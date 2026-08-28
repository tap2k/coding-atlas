from report.build import build, fmt_table
from report.utils import fmt_pct, slug


def test_fmt_pct():
    assert fmt_pct(0.256) == "25.6%"


def test_slug():
    assert slug("Big Site") == "big-site"


def test_build_contains_rate():
    assert "75.0%" in build("x", 3, 4)


def test_fmt_table():
    assert fmt_table([[1, 2]]) == "1 | 2"


def test_slug_again():
    assert slug("Big Site") == "big-site"
