import csv
from dataclasses import dataclass


@dataclass
class Row:
    date: str
    site: str
    count: int


def load(path: str) -> list[Row]:
    out = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            out.append(Row(r["date"], r["site"], int(r["count"])))
    return out
