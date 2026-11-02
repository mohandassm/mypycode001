"""
MERGE SORT  (divide and conquer)
Split in half, sort each half recursively, merge the two sorted halves.

Time O(n log n) always, Space O(n), Stable.

Interview tips
  - Great for linked lists and external sorting; explain T(n) = 2T(n/2) + O(n).
"""


def merge(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:           # <= keeps it stable
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    return out + a[i:] + b[j:]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def test():
    import random
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]
    assert merge_sort([]) == [] and merge_sort([1]) == [1]
    data = [random.randint(-50, 50) for _ in range(200)]
    assert merge_sort(data) == sorted(data)


if __name__ == "__main__":
    print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
    test()
    print("All tests passed")
