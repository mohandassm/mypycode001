"""
ROTATE ARRAY by k steps (right)
[1,2,3,4,5], k=2 -> [4,5,1,2,3].

Approaches
  1. Slicing nums[-k:] + nums[:-k]  -> O(n) time, O(n) space
  2. Reverse trick (in place)       -> O(n) time, O(1) space   <- impressive answer
     reverse all, reverse first k, reverse the rest.

Interview tips
  - Always do k %= n first (k can be larger than n).
"""


def rotate_slice(nums, k):
    if not nums:
        return nums
    k %= len(nums)
    return nums[-k:] + nums[:-k] if k else nums[:]


def rotate_in_place(nums, k):
    n = len(nums)
    if n == 0:
        return nums
    k %= n

    def rev(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

    rev(0, n - 1)
    rev(0, k - 1)
    rev(k, n - 1)
    return nums


def test():
    assert rotate_slice([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate_slice([1, 2, 3], 5) == [2, 3, 1]
    assert rotate_in_place([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate_in_place([1, 2, 3], 0) == [1, 2, 3] and rotate_in_place([], 3) == []
    for k in range(10):
        assert rotate_slice(list(range(6)), k) == rotate_in_place(list(range(6)), k)


if __name__ == "__main__":
    print(rotate_in_place([1, 2, 3, 4, 5], 2))
    test()
    print("All tests passed")
