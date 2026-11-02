"""
MERGE TWO SORTED ARRAYS
[1,3,5] + [2,4] -> [1,2,3,4,5].

Approach : two pointers, always take the smaller front element.  O(n+m).
This is the "merge" step of merge sort.

Interview tips
  - LeetCode 88 variant merges IN PLACE into the first array from the BACK.
"""


def merge_sorted(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    return out + a[i:] + b[j:]


def merge_in_place(nums1, m, nums2, n):
    """nums1 has m real items followed by n empty slots. Fill from the back."""
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1


def test():
    assert merge_sorted([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]
    assert merge_sorted([], [1]) == [1] and merge_sorted([1], []) == [1]
    assert merge_in_place([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]


if __name__ == "__main__":
    print(merge_sorted([1, 3, 5], [2, 4]))
    test()
    print("All tests passed")
