"""
COUNT VOWELS / CONSONANTS
Approach : loop and check membership in a set (O(1) lookup). Time O(n).

Interview tips
  - Handle uppercase (lower() first) and ignore non-letters for consonants.
"""
VOWELS = set("aeiou")


def count_vowels(s):
    return sum(1 for c in s.lower() if c in VOWELS)


def count_consonants(s):
    return sum(1 for c in s.lower() if c.isalpha() and c not in VOWELS)


def test():
    assert count_vowels("Education") == 5
    assert count_consonants("Hello, World!") == 7
    assert count_vowels("") == 0 and count_vowels("xyz") == 0


if __name__ == "__main__":
    print(count_vowels("Education"), count_consonants("Hello, World!"))
    test()
    print("All tests passed")
