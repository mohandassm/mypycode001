"""
DUPLICATES: remove and find
Approaches
  1. dict.fromkeys / seen-set -> O(n), keeps order
  2. set()                    -> O(n), loses order
  3. Sorted array two-pointer -> O(n) time, O(1) space (LeetCode 26)

Interview tips
  - Ask whether order must be preserved.
  - Be ready to do it in place on a sorted array.
"""
from collections import Counter


def remove_duplicates(nums):
    return list(dict.fromkeys(nums))


def remove_duplicates_seen(nums):
    seen, out = set(), []
    for x in nums:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def remove_duplicates_sorted_inplace(nums):
    """Sorted input. Returns new length; nums[:length] holds unique values."""
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write


def find_duplicates(nums):
    return [k for k, v in Counter(nums).items() if v > 1]


def test():
    assert remove_duplicates([1, 2, 1, 3, 2]) == remove_duplicates_seen([1, 2, 1, 3, 2]) == [1, 2, 3]
    arr = [1, 1, 2, 2, 2, 3]
    n = remove_duplicates_sorted_inplace(arr)
    assert n == 3 and arr[:n] == [1, 2, 3]
    assert find_duplicates([1, 2, 1, 3, 2, 2]) == [1, 2]
    assert remove_duplicates([]) == []


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 1, 3, 2]))
    test()
    print("All tests passed")
