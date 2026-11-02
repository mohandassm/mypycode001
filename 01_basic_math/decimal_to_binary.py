"""
DECIMAL <-> BINARY
Meaning : Convert base-10 to base-2 and back. 10 -> "1010".

Approach : divide by 2 repeatedly, collect remainders, reverse them. Time O(log n).

Interview tips
  - Know the built-ins (bin(), int(s, 2)) but be ready to write it manually.
  - Generalize to any base (2-16) - often asked as a follow-up.
"""


def decimal_to_binary(n):
    if n == 0:
        return "0"
    sign, n, bits = ("-" if n < 0 else ""), abs(n), []
    while n:
        bits.append(str(n % 2))
        n //= 2
    return sign + "".join(reversed(bits))


def binary_to_decimal(s):
    result = 0
    for ch in s:
        result = result * 2 + int(ch)
    return result


def to_base(n, base):
    digits = "0123456789ABCDEF"
    if n == 0:
        return "0"
    out = []
    while n:
        out.append(digits[n % base])
        n //= base
    return "".join(reversed(out))


def test():
    for n in range(0, 500):
        assert decimal_to_binary(n) == bin(n)[2:]
        assert binary_to_decimal(decimal_to_binary(n)) == n
    assert decimal_to_binary(-10) == "-1010"
    assert to_base(255, 16) == "FF" and to_base(8, 8) == "10"


if __name__ == "__main__":
    print(decimal_to_binary(10), binary_to_decimal("1010"), to_base(255, 16))
    test()
    print("All tests passed")
