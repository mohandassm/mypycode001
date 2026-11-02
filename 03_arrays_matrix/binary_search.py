"""
BINARY SEARCH
Meaning : On a SORTED list, repeatedly halve the search range.

Time O(log n).  Space O(1) iterative, O(log n) recursive.

Interview tips
  - Input MUST be sorted - say it out loud.
  - Use mid = low + (high - low) // 2 in C/Java to avoid overflow.
  - Common bugs: infinite loop (wrong low/high update), off-by-one (low <= high).
  - Variants asked often: first/last occurrence, insert position (bisect), rotated array.
"""


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    return binary_search_recursive(arr, target, low, mid - 1)


def first_occurrence(arr, target):
    """Leftmost index of target (duplicates allowed)."""
    low, high, ans = 0, len(arr) - 1, -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            ans, high = mid, mid - 1        # keep searching left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return ans


def insert_position(arr, target):
    """Index where target is or should be inserted (like bisect_left)."""
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


def test():
    s = [1, 3, 5, 7, 9, 11]
    for i, v in enumerate(s):
        assert binary_search(s, v) == binary_search_recursive(s, v) == i
    assert binary_search(s, 4) == -1 and binary_search([], 1) == -1
    assert first_occurrence([1, 2, 2, 2, 3], 2) == 1 and first_occurrence([1, 3], 2) == -1
    assert insert_position(s, 6) == 3 and insert_position(s, 0) == 0 and insert_position(s, 99) == 6


if __name__ == "__main__":
    print(binary_search([1, 3, 5, 7, 9], 7))
    test()
    print("All tests passed")
