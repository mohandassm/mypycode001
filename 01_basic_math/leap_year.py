"""
LEAP YEAR
Rule : divisible by 4, EXCEPT centuries - those must be divisible by 400.
       2000 -> leap,  1900 -> not leap,  2024 -> leap.

Interview tips
  - Many people forget the century rule. State it clearly before coding.
"""


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def test():
    assert is_leap_year(2000) and is_leap_year(2024) and is_leap_year(1996)
    assert not is_leap_year(1900) and not is_leap_year(2023) and not is_leap_year(2100)


if __name__ == "__main__":
    print([y for y in range(1990, 2030) if is_leap_year(y)])
    test()
    print("All tests passed")
