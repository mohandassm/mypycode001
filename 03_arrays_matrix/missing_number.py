"""
MISSING NUMBER
Array has numbers 0..n with exactly one missing.  [3,0,1] -> 2.

Approaches
  1. Sum formula n(n+1)/2 - sum(arr)  -> O(n) time, O(1) space
  2. XOR of indices and values        -> O(n), no overflow worry
  3. Set difference                   -> O(n) space

Interview tips
  - Mention XOR trick: a ^ a = 0, so everything cancels except the missing one.
"""


def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


def missing_number_xor(nums):
    result = len(nums)
    for i, x in enumerate(nums):
        result ^= i ^ x
    return result


def missing_number_set(nums):
    return (set(range(len(nums) + 1)) - set(nums)).pop()


def test():
    for f in (missing_number, missing_number_xor, missing_number_set):
        assert f([3, 0, 1]) == 2
        assert f([0, 1]) == 2
        assert f([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
        assert f([0]) == 1


if __name__ == "__main__":
    print(missing_number([3, 0, 1]))
    test()
    print("All tests passed")
