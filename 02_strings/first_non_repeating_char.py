"""
FIRST NON-REPEATING CHARACTER
"swiss" -> "w".   "aabb" -> None.

Approach : pass 1 count characters, pass 2 return first with count 1.  O(n) time.

Interview tips
  - Two passes is fine - say it is still O(n).
  - Dicts keep insertion order in Python 3.7+, so you can also scan the dict.
"""
from collections import Counter


def first_non_repeating_char(s):
    counts = Counter(s)
    for c in s:
        if counts[c] == 1:
            return c
    return None


def first_non_repeating_index(s):
    counts = Counter(s)
    for i, c in enumerate(s):
        if counts[c] == 1:
            return i
    return -1


def test():
    assert first_non_repeating_char("swiss") == "w"
    assert first_non_repeating_char("aabb") is None and first_non_repeating_char("") is None
    assert first_non_repeating_index("leetcode") == 0
    assert first_non_repeating_index("loveleetcode") == 2


if __name__ == "__main__":
    print(first_non_repeating_char("swiss"))
    test()
    print("All tests passed")
