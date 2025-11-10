import pytest
from src.is_palindrome import is_palindrome

@pytest.mark.parametrize("s,expected", [
    ("racecar", True),
    ("RaceCar", True),
    ("A man, a plan, a canal: Panama!", True),
    ("hello", False),
    ("", True),
])
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected