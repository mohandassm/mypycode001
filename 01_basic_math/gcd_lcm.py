"""
GCD (HCF) and LCM
Meaning : GCD = largest number dividing both.  LCM = smallest number both divide.
          gcd(48,18)=6,  lcm(4,6)=12.   Identity: gcd(a,b) * lcm(a,b) = a * b.

Approaches
  1. Loop down from min(a,b)   -> O(min)
  2. Euclid's algorithm        -> O(log min)   <- expected answer

Interview tips
  - Euclid: gcd(a, b) = gcd(b, a % b) until b == 0.
  - Compute LCM via GCD:  a*b // gcd(a,b)  (divide first to avoid overflow in C/Java).
"""
import math
from functools import reduce


def gcd_brute(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a, b):
    return abs(a // gcd(a, b) * b) if a and b else 0


def gcd_list(nums):
    return reduce(gcd, nums)


def lcm_list(nums):
    return reduce(lcm, nums)


def test():
    assert gcd(48, 18) == 6 == gcd_brute(48, 18) == math.gcd(48, 18)
    assert gcd(7, 13) == 1 and gcd(0, 5) == 5
    assert lcm(4, 6) == 12 and lcm(0, 5) == 0
    assert gcd_list([12, 18, 24]) == 6
    assert lcm_list([1, 2, 3, 4, 5]) == 60


if __name__ == "__main__":
    print("gcd(48,18) =", gcd(48, 18), "| lcm(4,6) =", lcm(4, 6))
    test()
    print("All tests passed")
