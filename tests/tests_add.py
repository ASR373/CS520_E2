import pytest
from src.add import add

@pytest.mark.parametrize("args,expected", [
    ((1, 2), 3),
    ((-5, 5), 0),
    ((0, 0), 0),
    ((10**6, 10**6), 2*10**6),
])
def test_add(args, expected):
    assert add(*args) == expected
