from typing import Iterable

def sum_of_squares(xs: Iterable[int]) -> int:
    """Return the sum of squares of the given iterable of numbers."""
    return sum(x * x for x in xs)
