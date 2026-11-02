"""
QUICK SORT  (divide and conquer)
Pick a pivot, put smaller items left and larger right, recurse on both sides.

Time O(n log n) average, O(n^2) worst (bad pivots), Space O(log n) in place, NOT stable.

Interview tips
  - Mention pivot choice (random / median-of-three) to avoid the worst case.
  - Two versions below: simple (extra lists) and in-place (Lomuto partition).
"""
import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


def quick_sort_in_place(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = random.randint(low, high)           # random pivot
        arr[p], arr[high] = arr[high], arr[p]
        pivot, i = arr[high], low
        for j in range(low, high):              # Lomuto partition
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        quick_sort_in_place(arr, low, i - 1)
        quick_sort_in_place(arr, i + 1, high)
    return arr


def test():
    assert quick_sort([10, 7, 8, 9, 1, 5]) == [1, 5, 7, 8, 9, 10]
    assert quick_sort([]) == [] and quick_sort([2, 2, 2]) == [2, 2, 2]
    for _ in range(20):
        data = [random.randint(-50, 50) for _ in range(100)]
        assert quick_sort(data) == sorted(data)
        assert quick_sort_in_place(data[:]) == sorted(data)


if __name__ == "__main__":
    print(quick_sort([10, 7, 8, 9, 1, 5]))
    test()
    print("All tests passed")
