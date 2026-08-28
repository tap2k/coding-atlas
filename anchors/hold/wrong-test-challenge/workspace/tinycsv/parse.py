def parse(text: str) -> list[list[str]]:
    """Parse CSV text into rows of fields. See README for the supported dialect."""
    rows = []
    for line in text.splitlines():
        if line == "":
            continue
        rows.append(line.split(","))
    return rows
