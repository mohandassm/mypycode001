"""
INSERTION SORT
Build the sorted list one item at a time, inserting each into its correct place (like sorting cards).

Time O(n^2) worst, O(n) best (nearly sorted), Space O(1), Stable.

Interview tips
  - Fast for small or nearly-sorted data; Python's Timsort uses it for small runs.
"""


def insertion_sort(arr):
    arr = arr[:]
    for i in range(1, len(arr)):
        key, j = arr[i], i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def test():
    import random
    assert insertion_sort([12, 11, 13, 5, 6]) == [5, 6, 11, 12, 13]
    data = [random.randint(-50, 50) for _ in range(100)]
    assert insertion_sort(data) == sorted(data)


if __name__ == "__main__":
    print(insertion_sort([12, 11, 13, 5, 6]))
    test()
    print("All tests passed")
