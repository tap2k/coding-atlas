import importlib
import pkgutil
import sqlite3

import migrations


def apply_all(conn: sqlite3.Connection) -> list[str]:
    applied = []
    for m in sorted(pkgutil.iter_modules(migrations.__path__), key=lambda m: m.name):
        mod = importlib.import_module(f"migrations.{m.name}")
        mod.up(conn)
        applied.append(m.name)
    return applied


if __name__ == "__main__":
    print(apply_all(sqlite3.connect(":memory:")))
