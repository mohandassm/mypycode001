"""
LONGEST PALINDROMIC SUBSTRING
"babad" -> "bab" (or "aba").

Approaches
  1. Check all substrings                -> O(n^3)
  2. Expand around each center (odd+even) -> O(n^2), O(1) space  <- expected
  3. Manacher algorithm                           -> O(n)  (mention only)

Interview tips
  - Remember BOTH center types: single char (odd) and between two chars (even).
"""


def longest_palindrome(s):
    if not s:
        return ""
    best = ""
    for c in range(len(s)):
        for l, r in ((c, c), (c, c + 1)):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > len(best):
                best = s[l + 1:r]
    return best


def test():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a" and longest_palindrome("") == ""
    assert longest_palindrome("forgeeksskeegfor") == "geeksskeeg"


if __name__ == "__main__":
    print(longest_palindrome("forgeeksskeegfor"))
    test()
    print("All tests passed")
