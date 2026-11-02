"""
SELECTION SORT
Find the minimum of the unsorted part, swap it to the front.

Time O(n^2) always, Space O(1), NOT stable, at most n-1 swaps.

Interview tips
  - Good when writes are expensive (few swaps).
"""


def selection_sort(arr):
    arr = arr[:]
    for i in range(len(arr)):
        m = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]
    return arr


def test():
    import random
    assert selection_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]
    data = [random.randint(-50, 50) for _ in range(100)]
    assert selection_sort(data) == sorted(data)


if __name__ == "__main__":
    print(selection_sort([64, 25, 12, 22, 11]))
    test()
    print("All tests passed")
