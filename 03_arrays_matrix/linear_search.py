"""
LINEAR SEARCH
Meaning : Check every element from start to end until found.

Time O(n) worst, O(1) best.  Space O(1).  Works on UNSORTED data.

Interview tips
  - Use it when data is unsorted/small. Contrast with binary search (needs sorted).
  - Return -1 (or None) when not found - state your convention.
"""


def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


def linear_search_all(arr, target):
    return [i for i, v in enumerate(arr) if v == target]


def test():
    data = [4, 2, 9, 2, 7]
    assert linear_search(data, 9) == 2 and linear_search(data, 2) == 1
    assert linear_search(data, 100) == -1 and linear_search([], 1) == -1
    assert linear_search_all(data, 2) == [1, 3]


if __name__ == "__main__":
    print(linear_search([4, 2, 9, 7], 9))
    test()
    print("All tests passed")
