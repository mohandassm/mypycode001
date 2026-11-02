"""
BUBBLE SORT
Repeatedly swap adjacent out-of-order items; largest value "bubbles" to the end each pass.

Time O(n^2) (O(n) best with early exit), Space O(1), Stable.

Interview tips
  - Add the `swapped` flag optimization - interviewers look for it.
  - Never use it in production; know why it is slow.
"""


def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def test():
    import random
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert bubble_sort([]) == [] and bubble_sort([1]) == [1]
    data = [random.randint(-50, 50) for _ in range(100)]
    assert bubble_sort(data) == sorted(data)


if __name__ == "__main__":
    print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
    test()
    print("All tests passed")
