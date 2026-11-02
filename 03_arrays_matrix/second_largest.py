"""
SECOND LARGEST ELEMENT
[10, 5, 20, 8] -> 10.

Approaches
  1. sort and pick               -> O(n log n)
  2. Single pass, two variables  -> O(n) time, O(1) space   <- expected

Interview tips
  - Handle duplicates ([5,5,5] has no second largest) and arrays shorter than 2.
  - Generalize to k-th largest: heapq.nlargest or quickselect.
"""
import heapq


def second_largest(nums):
    first = second = None
    for x in nums:
        if first is None or x > first:
            first, second = x, first
        elif x != first and (second is None or x > second):
            second = x
    return second


def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]


def test():
    assert second_largest([10, 5, 20, 8]) == 10
    assert second_largest([20, 20, 10]) == 10
    assert second_largest([5, 5, 5]) is None and second_largest([1]) is None
    assert second_largest([-1, -5, -3]) == -3
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5


if __name__ == "__main__":
    print(second_largest([10, 5, 20, 8]))
    test()
    print("All tests passed")
