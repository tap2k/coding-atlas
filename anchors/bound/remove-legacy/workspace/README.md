# report-export

Exports the daily report. `python cli.py --out report.csv` writes CSV. `pytest` to test.

The legacy exporter (`python cli.py --legacy`, or `python -m export.legacy`) writes the
pre-2025 pipe-delimited format that the old finance importer reads.
