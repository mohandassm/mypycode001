"""
TWO SUM
Find two indices whose values add up to target.  [2,7,11,15], 9 -> (0, 1).

Approaches
  1. Brute force, two loops              -> O(n^2)
  2. Hash map of seen values (one pass)  -> O(n) time, O(n) space   <- expected
  3. Sorted array + two pointers         -> O(n) time, O(1) space

Interview tips
  - For each x look up (target - x) in the map BEFORE inserting x (handles duplicates).
  - Ask: exactly one solution? Can I reuse the same element? Is it sorted?
"""


def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return (seen[target - x], i)
        seen[x] = i
    return None


def two_sum_sorted(nums, target):
    """Input sorted ascending; returns the values."""
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return (nums[l], nums[r])
        if s < target:
            l += 1
        else:
            r -= 1
    return None


def test():
    assert two_sum([2, 7, 11, 15], 9) == (0, 1) == two_sum_brute([2, 7, 11, 15], 9)
    assert two_sum([3, 3], 6) == (0, 1)
    assert two_sum([3, 2, 4], 6) == (1, 2)
    assert two_sum([1, 2], 10) is None
    assert two_sum_sorted([1, 2, 4, 7, 11], 9) == (2, 7)


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    test()
    print("All tests passed")
