import argparse

from export import export_csv, export_legacy

ap = argparse.ArgumentParser()
ap.add_argument("--out", default="report.csv")
ap.add_argument("--legacy", action="store_true", help="pipe-delimited pre-2025 format")
a = ap.parse_args()
n = export_legacy(a.out) if a.legacy else export_csv(a.out)
print(f"wrote {n} rows to {a.out}")
