"""
SUB-STRING
Meaning : A contiguous sequence of characters inside a string. "press" in "expression".
          (A SUBSEQUENCE is different: order kept, but need not be contiguous.)

Facts : a string of length n has n(n+1)/2 non-empty substrings.

Interview tips
  - Know substring vs subsequence - interviewers test this.
  - Naive search is O(n*m); mention KMP / Rabin-Karp as O(n+m) improvements.
"""


def all_substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]


def is_substring(sub, s):
    """Manual search, no `in` operator."""
    n, m = len(s), len(sub)
    for i in range(n - m + 1):
        if s[i:i + m] == sub:
            return True
    return m == 0


def find_index(sub, s):
    for i in range(len(s) - len(sub) + 1):
        if s[i:i + len(sub)] == sub:
            return i
    return -1


def count_occurrences(sub, s):
    return sum(1 for i in range(len(s) - len(sub) + 1) if s[i:i + len(sub)] == sub)


def is_subsequence(sub, s):
    it = iter(s)
    return all(ch in it for ch in sub)


def test():
    assert all_substrings("abc") == ["a", "ab", "abc", "b", "bc", "c"]
    n = 7
    assert len(all_substrings("a" * n)) == n * (n + 1) // 2
    assert is_substring("press", "expression") and not is_substring("xyz", "expression")
    assert find_index("press", "expression") == 2 and find_index("z", "abc") == -1
    assert count_occurrences("aa", "aaaa") == 3
    assert is_subsequence("ace", "abcde") and not is_subsequence("aec", "abcde")


if __name__ == "__main__":
    print(all_substrings("abc"), is_substring("press", "expression"))
    test()
    print("All tests passed")
