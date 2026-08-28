import re

_NON_WORD = re.compile(r"[^a-z0-9]+")


def slugify(text: str, sep: str = "-") -> str:
    """Lowercase, replace runs of non-alphanumerics with `sep`, trim."""
    text = text.lower()
    text = _NON_WORD.sub(sep, text)
    return text.strip(sep)
