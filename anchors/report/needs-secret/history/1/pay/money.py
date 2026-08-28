def to_cents(amount: str) -> int:
    """'12.34' -> 1234. Rejects more than two decimals."""
    whole, _, frac = amount.partition(".")
    if len(frac) > 2:
        raise ValueError("too many decimal places")
    return int(whole) * 100 + int(frac or 0)
