from .data import rows


def export_csv(path: str) -> int:
    with open(path, "w") as f:
        f.write("date,site,count\n")
        for d, s, c in rows():
            f.write(f"{d},{s},{c}\n")
    return len(rows())
