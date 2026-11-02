"""
CHARACTER FREQUENCY  (+ most common / duplicates)
Approaches
  1. dict with .get()      -> O(n)
  2. collections.Counter   -> O(n)   <- idiomatic

Interview tips
  - This is the building block for anagram, first-unique-char, duplicates.
  - Know when to use dict vs fixed array (26 letters).
"""
from collections import Counter


def char_frequency_manual(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq


def char_frequency(s):
    return dict(Counter(s))


def most_common_char(s):
    return Counter(s).most_common(1)[0] if s else None


def duplicate_chars(s):
    return [c for c, n in Counter(s).items() if n > 1]


def test():
    assert char_frequency_manual("hello") == char_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert most_common_char("hello") == ("l", 2) and most_common_char("") is None
    assert duplicate_chars("programming") == ["r", "g", "m"]


if __name__ == "__main__":
    print(char_frequency("hello"), most_common_char("hello"))
    test()
    print("All tests passed")
