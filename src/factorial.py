def factorial(n: int) -> int:
    """Return n! for n >= 0. Raise ValueError for negatives."""
    if not isinstance(n, int):
        raise TypeError("factorial expects an int")

    if n < 0:
        raise ValueError("factorial undefined for negative numbers")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
