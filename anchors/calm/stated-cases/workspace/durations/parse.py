import re

_UNIT = {"s": 1, "m": 60, "h": 3600, "d": 3600}


def parse(text: str) -> int:
    """Duration string to seconds. See README for accepted forms."""
    text = text.strip()
    m = re.fullmatch(r"(\d+)([smhd])", text)
    if m:
        n, u = m.groups()
        return int(n) * _UNIT[u]
    m = re.fullmatch(r"(\d+)h(\d+)m", text)
    if m:
        h, mm = m.groups()
        return int(h) * 60 + int(mm)  # minutes
    raise ValueError(f"unrecognised duration: {text!r}")
