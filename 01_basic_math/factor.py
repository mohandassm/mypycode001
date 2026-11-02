"""
FACTOR
Meaning : A number that divides another number perfectly (remainder 0). 3 is a factor of 6.

Approaches
  1. Brute force  : test 1..n                -> O(n)
  2. Optimized    : test 1..sqrt(n), collect pairs (i, n//i) -> O(sqrt n)

Interview tips
  - Factors always come in pairs, so you only need to go up to sqrt(n).
  - Watch the perfect-square case (36 -> 6 x 6): don't add 6 twice.
  - Related questions: prime factorization, count of factors, sum of factors.
"""
import math


def factors_brute(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def factors(n):
    """Optimized O(sqrt n), returns sorted list."""
    if n <= 0:
        raise ValueError("n must be positive")
    small, large = [], []
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            small.append(i)
            if i != n // i:          # avoid duplicate for perfect squares
                large.append(n // i)
    return small + large[::-1]


def prime_factors(n):
    """Prime factorization: 60 -> [2, 2, 3, 5]. Common follow-up question."""
    result, d = [], 2
    while d * d <= n:
        while n % d == 0:
            result.append(d)
            n //= d
        d += 1
    if n > 1:
        result.append(n)
    return result


def test():
    assert factors(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36]
    assert factors(1) == [1]
    assert factors(36) == factors_brute(36)
    assert prime_factors(60) == [2, 2, 3, 5]
    assert prime_factors(97) == [97]


if __name__ == "__main__":
    print("factors(36)       :", factors(36))
    print("prime_factors(60) :", prime_factors(60))
    test()
    print("All tests passed")
