"""
FACTORIAL
Meaning : n! = n x (n-1) x ... x 1.  4! = 24.  0! = 1 (by definition).

Approaches
  1. Iterative  -> O(n) time, O(1) space
  2. Recursive  -> O(n) time, O(n) call stack (recursion limit ~1000 in Python)
  3. math.factorial (built-in)

Interview tips
  - Mention the base case 0! = 1 and reject negative numbers.
  - Related: trailing zeros in n! = count of factors of 5 (n//5 + n//25 + ...).
"""
import math


def factorial_iter(n):
    if n < 0:
        raise ValueError("negative numbers have no factorial")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_rec(n):
    if n < 0:
        raise ValueError("negative numbers have no factorial")
    return 1 if n <= 1 else n * factorial_rec(n - 1)


def trailing_zeros(n):
    """Trailing zeros of n! without computing it. Classic follow-up."""
    count, p = 0, 5
    while p <= n:
        count += n // p
        p *= 5
    return count


def test():
    for n in range(0, 15):
        assert factorial_iter(n) == factorial_rec(n) == math.factorial(n)
    assert factorial_iter(4) == 24
    assert trailing_zeros(100) == 24
    try:
        factorial_iter(-1)
        assert False
    except ValueError:
        pass


if __name__ == "__main__":
    print("5! =", factorial_iter(5), "| trailing zeros of 100! =", trailing_zeros(100))
    test()
    print("All tests passed")
