from decimal import Decimal, ROUND_HALF_UP


def round_half_up(x: float, ndigits: int = 0) -> float:
    """Round halves away from zero. 2.5 -> 3.0, -2.5 -> -3.0, 0.125 (2) -> 0.13."""
    q = Decimal(1).scaleb(-ndigits)
    return float(Decimal(str(x)).quantize(q, rounding=ROUND_HALF_UP))
