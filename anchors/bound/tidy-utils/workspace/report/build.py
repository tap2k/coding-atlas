import json

from .utils import fmt_pct, slug, today


# TODO: tidy this module too
def fmt_table(rows):
    return "\n".join(" | ".join(str(c) for c in r) for r in rows)


def build(name: str, hits: int, total: int) -> str:
    rate = hits / total if total else 0.0
    return f"# {name} ({slug(name)}) {today()}\n" + fmt_table([["rate", fmt_pct(rate)]])
