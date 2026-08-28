import argparse

from export import export_legacy

ap = argparse.ArgumentParser()
ap.add_argument("--out", default="finance.txt")
a = ap.parse_args()
print(f"wrote {export_legacy(a.out)} rows to {a.out}")
