def reverse_words(s: str) -> str:
    """
    Reverse the order of words, collapsing any extra whitespace.
    Examples:
      "hello world" -> "world hello"
      "  multiple   spaces here  " -> "here spaces multiple"
    """
    words = s.split()  # splits on any whitespace, collapses runs
    return " ".join(reversed(words))
