"""
ANAGRAM
Meaning : Word formed by rearranging letters of another. "listen" <-> "silent".

Approaches
  1. Sort both and compare        -> O(n log n)
  2. Count letters (Counter/dict) -> O(n)   <- best
  3. Fixed 26-slot array          -> O(n), O(1) space for lowercase a-z

Interview tips
  - Different lengths = instantly False.
  - Ask about case, spaces, unicode.
  - Follow-up: group anagrams (use sorted word as dict key) - included below.
"""
from collections import Counter, defaultdict


def is_anagram_sort(a, b):
    return sorted(a) == sorted(b)


def is_anagram(a, b):
    a, b = a.replace(" ", "").lower(), b.replace(" ", "").lower()
    return len(a) == len(b) and Counter(a) == Counter(b)


def is_anagram_array(a, b):
    """Lowercase a-z only, O(1) extra space."""
    if len(a) != len(b):
        return False
    counts = [0] * 26
    for x, y in zip(a, b):
        counts[ord(x) - 97] += 1
        counts[ord(y) - 97] -= 1
    return not any(counts)


def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups["".join(sorted(w))].append(w)
    return list(groups.values())


def test():
    assert is_anagram("listen", "silent") and is_anagram("Dormitory", "Dirty room")
    assert not is_anagram("abc", "abd") and not is_anagram("a", "ab")
    assert is_anagram_sort("listen", "silent") and is_anagram_array("listen", "silent")
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(map(sorted, result)) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]


if __name__ == "__main__":
    print(is_anagram("listen", "silent"))
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    test()
    print("All tests passed")
