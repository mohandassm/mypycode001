"""
ROTATE MATRIX 90 DEGREES
Clockwise     = transpose, then reverse each row.
Anticlockwise = transpose, then reverse the order of rows.

Interview tips
  - LeetCode 48 asks for IN-PLACE rotation of an n x n matrix (O(1) extra space).
"""


def rotate_clockwise(m):
    return [list(row)[::-1] for row in zip(*m)]


def rotate_anticlockwise(m):
    return [list(row) for row in zip(*m)][::-1]


def rotate_in_place(m):
    """n x n only: transpose in place, then reverse each row."""
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    for row in m:
        row.reverse()
    return m


def test():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert rotate_clockwise(m) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert rotate_anticlockwise(m) == [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
    assert rotate_in_place([r[:] for r in m]) == rotate_clockwise(m)
    assert rotate_clockwise([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]


if __name__ == "__main__":
    for row in rotate_clockwise([[1, 2, 3], [4, 5, 6], [7, 8, 9]]):
        print(row)
    test()
    print("All tests passed")
