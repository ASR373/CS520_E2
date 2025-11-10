from src.reverse_words import reverse_words

def test_reverse_words():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("  multiple   spaces here  ") == "here spaces multiple"
    assert reverse_words("") == ""
    assert reverse_words("one") == "one"
