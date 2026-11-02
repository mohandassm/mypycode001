"""
STRONG NUMBER
Meaning : Sum of the factorials of its digits equals the number.
          145 = 1! + 4! + 5! = 1 + 24 + 120.   Known: 1, 2, 145, 40585.

Interview tips
  - Precompute factorials 0..9 once instead of recalculating for each digit.
"""
FACT = [1]
for _i in range(1, 10):
    FACT.append(FACT[-1] * _i)


def is_strong(n):
    if n <= 0:
        return False
    total, temp = 0, n
    while temp:
        total += FACT[temp % 10]
        temp //= 10
    return total == n


def test():
    assert [n for n in range(1, 50000) if is_strong(n)] == [1, 2, 145, 40585]


if __name__ == "__main__":
    print([n for n in range(1, 50000) if is_strong(n)])
    test()
    print("All tests passed")
