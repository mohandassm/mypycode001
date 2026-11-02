"""
POWER OF TWO  (+ bit tricks)
Meaning : n = 2^k.  1, 2, 4, 8, 16 ...

Approaches
  1. Divide by 2 repeatedly     -> O(log n)
  2. Bit trick n & (n-1) == 0   -> O(1)   <- powers of two have exactly one set bit

Interview tips
  - Explain WHY: 8 = 1000, 7 = 0111, 8 & 7 = 0.
  - Also know: count set bits, check odd/even with n & 1, swap with XOR.
"""


def is_power_of_two_loop(n):
    if n < 1:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1


def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


def count_set_bits(n):
    """Brian Kernighan: each step removes the lowest set bit."""
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


def test():
    for n in range(-5, 2000):
        assert is_power_of_two(n) == is_power_of_two_loop(n)
    assert is_power_of_two(1024) and not is_power_of_two(0) and not is_power_of_two(6)
    assert count_set_bits(0b10110111) == 6 == bin(0b10110111).count("1")


if __name__ == "__main__":
    print([n for n in range(1, 100) if is_power_of_two(n)])
    test()
    print("All tests passed")
