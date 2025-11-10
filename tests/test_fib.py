import pytest
from src.fib import fib

@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (10, 55),
    (20, 6765),
])
def test_fib(n, expected):
    assert fib(n) == expected

def test_fib_negative():
    with pytest.raises(ValueError):
        fib(-3)
