import pytest
from src.factorial import factorial

@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (8, 40320),
])
def test_factorial(n, expected):
    assert factorial(n) == expected

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

# Additional factorial tests
import pytest
from src.factorial import factorial

def test_factorial_two():
    assert factorial(2) == 2

def test_factorial_large():
    assert factorial(10) == 3628800

@pytest.mark.parametrize("bad_input", [3.5, "5", None, [3]])
def test_factorial_type_error(bad_input):
    with pytest.raises(TypeError):
        factorial(bad_input)

def test_factorial_bool():
    assert factorial(True) == 1