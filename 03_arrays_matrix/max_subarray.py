"""
MAXIMUM SUBARRAY (Kadane's Algorithm)
Largest sum of a contiguous subarray.  [-2,1,-3,4,-1,2,1,-5,4] -> 6  ([4,-1,2,1]).

Approaches
  1. All subarrays       -> O(n^2)
  2. Kadane (DP)         -> O(n) time, O(1) space   <- expected

Idea : at each element, either extend the running sum or start fresh:
       current = max(x, current + x)

Interview tips
  - Works with all-negative arrays (answer = the largest single element).
  - Follow-up: return the subarray too (included below).
"""


def max_subarray_brute(nums):
    best = nums[0]
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            best = max(best, total)
    return best


def max_subarray(nums):
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


def max_subarray_with_indices(nums):
    best, cur = nums[0], nums[0]
    start = best_start = best_end = 0
    for i in range(1, len(nums)):
        if nums[i] > cur + nums[i]:
            cur, start = nums[i], i
        else:
            cur += nums[i]
        if cur > best:
            best, best_start, best_end = cur, start, i
    return best, nums[best_start:best_end + 1]


def test():
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray(a) == max_subarray_brute(a) == 6
    assert max_subarray([-3, -1, -2]) == -1 and max_subarray([5]) == 5
    assert max_subarray_with_indices(a) == (6, [4, -1, 2, 1])


if __name__ == "__main__":
    print(max_subarray_with_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    test()
    print("All tests passed")
