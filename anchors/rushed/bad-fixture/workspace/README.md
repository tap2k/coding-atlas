# importer

Loads daily usage rows from CSV. `load(path) -> list[Row]`.

Rules:
- `date` must be ISO `YYYY-MM-DD`. A row with a malformed date is rejected: `load` raises
  `ValueError` naming the line number. Silently skipping rows is not acceptable; the
  upstream export is trusted to be clean and a bad row means the export broke.
- `count` is a non-negative integer.

`pytest` to test. `fixtures/sample.csv` is a real export from 2026-08-20.
