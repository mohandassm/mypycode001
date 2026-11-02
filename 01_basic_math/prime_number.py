"""
PRIME NUMBER
Meaning : A number > 1 divisible only by 1 and itself (2, 3, 5, 7 ...).

Approaches
  1. Brute force        : test 2..n-1            -> O(n)
  2. Square-root check  : test 2..sqrt(n)        -> O(sqrt n)   <- expected answer
  3. Sieve of Eratosthenes : all primes <= n     -> O(n log log n)

Interview tips
  - 0 and 1 are NOT prime. 2 is the only even prime.
  - Skip even numbers after checking 2 to halve the work.
  - If asked "print all primes up to N", use the Sieve, not is_prime in a loop.
"""
import math


def is_prime_brute(n):
    if n < 2:
        return False
    return all(n % i for i in range(2, n))


def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True


def sieve(n):
    """All primes <= n."""
    if n < 2:
        return []
    flags = [True] * (n + 1)
    flags[0] = flags[1] = False
    for i in range(2, math.isqrt(n) + 1):
        if flags[i]:
            for j in range(i * i, n + 1, i):   # start at i*i
                flags[j] = False
    return [i for i, p in enumerate(flags) if p]


def nth_prime(k):
    """k-th prime (1-indexed)."""
    count, n = 0, 1
    while count < k:
        n += 1
        if is_prime(n):
            count += 1
    return n


def test():
    first = [2, 3, 5, 7, 11, 13, 17, 19]
    assert [n for n in range(20) if is_prime(n)] == first
    assert [n for n in range(20) if is_prime_brute(n)] == first
    assert sieve(20) == first
    assert not is_prime(1) and not is_prime(0) and not is_prime(-7)
    assert is_prime(2) and is_prime(97) and not is_prime(91)  # 91 = 7*13
    assert nth_prime(10) == 29


if __name__ == "__main__":
    print("is_prime(29):", is_prime(29))
    print("sieve(50)   :", sieve(50))
    print("nth_prime(10):", nth_prime(10))
    test()
    print("All tests passed")
