"""
PALINDROME
Meaning : Reads the same backward as forward. "radar", 121, "A man, a plan, a canal: Panama".

Approaches
  1. Reverse and compare s == s[::-1]   -> O(n) time, O(n) space
  2. Two pointers from both ends        -> O(n) time, O(1) space   <- best

Interview tips
  - Ask: ignore case/spaces/punctuation? (LeetCode 125 does.)
  - Palindrome NUMBER without strings: reverse the digits and compare.
"""


def is_palindrome_simple(s):
    return s == s[::-1]


def is_palindrome(s):
    """Two pointers, ignores case and non-alphanumerics."""
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left, right = left + 1, right - 1
    return True


def is_palindrome_number(n):
    if n < 0:
        return False
    original, rev = n, 0
    while n:
        rev = rev * 10 + n % 10
        n //= 10
    return original == rev


def test():
    assert is_palindrome_simple("radar") and not is_palindrome_simple("hello")
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert is_palindrome("") and is_palindrome("a") and not is_palindrome("race a car")
    assert is_palindrome_number(121) and is_palindrome_number(0)
    assert not is_palindrome_number(-121) and not is_palindrome_number(10)


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"), is_palindrome_number(12321))
    test()
    print("All tests passed")
