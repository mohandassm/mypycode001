"""
ARMSTRONG NUMBER
Meaning : Equals the sum of its digits each raised to the number of digits.
          153 = 1^3 + 5^3 + 3^3.   9474 = 9^4 + 4^4 + 7^4 + 4^4.

Approach : get digit count, sum digit**count, compare.  Time O(d).

Interview tips
  - The power is the NUMBER OF DIGITS (not always 3) - common mistake.
  - Do it with math (n % 10, n // 10) if the interviewer bans str().
"""


def is_armstrong(n):
    if n < 0:
        return False
    power = len(str(n))
    return sum(int(d) ** power for d in str(n)) == n


def is_armstrong_math(n):
    """Without converting to string."""
    if n < 0:
        return False
    power, temp = 0, n
    while temp:
        power += 1
        temp //= 10
    total, temp = 0, n
    while temp:
        total += (temp % 10) ** power
        temp //= 10
    return total == n if n else True


def armstrong_in_range(low, high):
    return [n for n in range(low, high + 1) if is_armstrong(n)]


def test():
    assert is_armstrong(153) and is_armstrong(9474) and is_armstrong(0)
    assert not is_armstrong(154)
    assert armstrong_in_range(100, 1000) == [153, 370, 371, 407]
    assert all(is_armstrong(n) == is_armstrong_math(n) for n in range(0, 10000))


if __name__ == "__main__":
    print("Armstrong 1..10000:", armstrong_in_range(1, 10000))
    test()
    print("All tests passed")
