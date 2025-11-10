def fib(n: int) -> int:
    """Return the n-th Fibonacci number (0-indexed). Raise ValueError for negatives."""
    if not isinstance(n, int):
        raise TypeError("fib expects an int")
    if n < 0:
        raise ValueError("fib undefined for negative numbers")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
