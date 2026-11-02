"""
REVERSE A NUMBER  (+ sum of digits, count of digits)
Meaning : 1234 -> 4321.

Approach : repeatedly take last digit (n % 10), build result (rev*10 + digit), drop it (n // 10).

Interview tips
  - Handle negatives (keep the sign) and trailing zeros (120 -> 21).
  - In Java/C++ mention 32-bit overflow when reversing (LeetCode 7).
"""


def reverse_number(n):
    sign = -1 if n < 0 else 1
    n, rev = abs(n), 0
    while n:
        rev = rev * 10 + n % 10
        n //= 10
    return sign * rev


def sum_of_digits(n):
    n, total = abs(n), 0
    while n:
        total += n % 10
        n //= 10
    return total


def count_digits(n):
    n = abs(n)
    count = 1 if n == 0 else 0
    while n:
        count += 1
        n //= 10
    return count


def test():
    assert reverse_number(1234) == 4321
    assert reverse_number(-120) == -21
    assert reverse_number(0) == 0
    assert sum_of_digits(1234) == 10 and sum_of_digits(-99) == 18
    assert count_digits(0) == 1 and count_digits(98765) == 5


if __name__ == "__main__":
    print(reverse_number(1234), sum_of_digits(1234), count_digits(1234))
    test()
    print("All tests passed")
