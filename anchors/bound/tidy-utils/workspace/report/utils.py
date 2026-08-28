import os
import sys
from datetime import date


def today() -> str:
    return date.today().isoformat()


def fmt_pct(x: float) -> str:
    return f"{x * 100:.1f}%"


# def fmt_pct_old(x):
#     return str(round(x * 100)) + "%"


def old_format(rows):
    # superseded by fmt_table in build.py
    return "\n".join(",".join(str(c) for c in r) for r in rows)


def chunk(items, n):
    return [items[i:i + n] for i in range(0, len(items), n)]


def safe_div(a, b):
    return a / b if b else 0.0


def percentile(values, p):
    s = sorted(values)
    k = max(0, min(len(s) - 1, round(p / 100 * (len(s) - 1))))
    return s[k]


def clamp(x, lo, hi):
    return max(lo, min(hi, x))


def slug(s: str) -> str:
    return s.lower().replace(" ", "-")
