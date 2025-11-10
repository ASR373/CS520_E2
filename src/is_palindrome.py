import string

def is_palindrome(s: str) -> bool:
    """Case-insensitive, alphanumeric-only palindrome check."""
    filtered = "".join(ch.lower() for ch in s if ch.isalnum())
    return filtered == filtered[::-1]
