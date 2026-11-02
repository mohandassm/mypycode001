"""
PERFECT NUMBER
Meaning : Equals the sum of its proper divisors (all factors except itself).
          6 = 1+2+3,  28 = 1+2+4+7+14.   Known: 6, 28, 496, 8128, 33550336 ...

Approaches
  1. Loop 1..n//2          -> O(n)
  2. Divisor pairs to sqrt -> O(sqrt n)   <- better

Interview tips
  - 1 is NOT perfect (no proper divisors besides itself).
  - Reuse your factor logic - shows clean thinking.
"""
import math


def is_perfect_brute(n):
    return n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) == n


def is_perfect(n):
    if n < 2:
        return False
    total = 1                                  # 1 is always a proper divisor
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total == n


def test():
    assert [n for n in range(1, 10000) if is_perfect(n)] == [6, 28, 496, 8128]
    assert all(is_perfect(n) == is_perfect_brute(n) for n in range(1, 2000))
    assert not is_perfect(1) and not is_perfect(12)


if __name__ == "__main__":
    print("Perfect numbers < 10000:", [n for n in range(1, 10000) if is_perfect(n)])
    test()
    print("All tests passed")
