"""
FIBONACCI SEQUENCE
Meaning : Each number is the sum of the previous two: 0, 1, 1, 2, 3, 5, 8 ...

Approaches
  1. Naive recursion         -> O(2^n)  (too slow, but interviewers ask it)
  2. Recursion + memoization -> O(n) time, O(n) space
  3. Iterative (two vars)    -> O(n) time, O(1) space   <- best
  4. Generator               -> lazy, memory friendly

Interview tips
  - Always mention that naive recursion repeats work (exponential).
  - Say "memoization / dynamic programming" to show you know the fix.
  - Python big ints never overflow; in Java/C++ mention long overflow at fib(93).
"""
from functools import lru_cache


def fib_naive(n):
    return n if n < 2 else fib_naive(n - 1) + fib_naive(n - 2)


@lru_cache(maxsize=None)
def fib_memo(n):
    return n if n < 2 else fib_memo(n - 1) + fib_memo(n - 2)


def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_series(count):
    """First `count` Fibonacci numbers."""
    return [fib_iter(i) for i in range(count)]


def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def test():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fib_series(10) == expected
    assert [fib_naive(i) for i in range(10)] == expected
    assert [fib_memo(i) for i in range(10)] == expected
    gen = fib_generator()
    assert [next(gen) for _ in range(10)] == expected
    assert fib_iter(50) == 12586269025


if __name__ == "__main__":
    print("series(10):", fib_series(10))
    print("fib_iter(50):", fib_iter(50))
    test()
    print("All tests passed")
