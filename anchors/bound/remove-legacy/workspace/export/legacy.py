import sys

from .data import rows


def export_legacy(path: str) -> int:
    with open(path, "w") as f:
        for d, s, c in rows():
            f.write(f"{d.replace('-', '')}|{s.upper()}|{c:06d}\n")
    return len(rows())


if __name__ == "__main__":
    print(export_legacy(sys.argv[1] if len(sys.argv) > 1 else "legacy.txt"))
