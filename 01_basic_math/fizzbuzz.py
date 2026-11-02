"""
FIZZBUZZ
Meaning : For 1..n print Fizz if divisible by 3, Buzz if by 5, FizzBuzz if both, else number.

Interview tips
  - Check the "both" case (15) FIRST, or use string concatenation.
  - Show you can make it extensible: pass rules as data (see fizzbuzz_rules).
"""


def fizzbuzz(n):
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out


def fizzbuzz_rules(n, rules=((3, "Fizz"), (5, "Buzz"))):
    """Extensible: add (7, 'Bazz') without touching the logic."""
    return ["".join(word for d, word in rules if i % d == 0) or str(i)
            for i in range(1, n + 1)]


def test():
    assert fizzbuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz",
                            "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    assert fizzbuzz(30) == fizzbuzz_rules(30)
    assert fizzbuzz_rules(7, ((3, "Fizz"), (5, "Buzz"), (7, "Bazz")))[-1] == "Bazz"


if __name__ == "__main__":
    print(fizzbuzz(15))
    test()
    print("All tests passed")
