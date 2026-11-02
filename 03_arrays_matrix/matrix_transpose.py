"""
MATRIX TRANSPOSE
Meaning : Flip a 2D grid over its diagonal - rows become columns.
          [[1,2,3],[4,5,6]] -> [[1,4],[2,5],[3,6]]

Approaches
  1. Nested loops / list comprehension -> O(r*c) time, new matrix
  2. zip(*matrix)                       -> Pythonic one-liner
  3. In-place for SQUARE matrices (swap m[i][j] with m[j][i], j > i) -> O(1) space

Interview tips
  - Result shape is c x r for an r x c input.
  - Transpose + reverse each row = rotate 90 degrees clockwise (see matrix_rotate.py).
"""


def transpose(matrix):
    if not matrix:
        return []
    return [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]


def transpose_zip(matrix):
    return [list(row) for row in zip(*matrix)]


def transpose_in_place(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def test():
    m = [[1, 2, 3], [4, 5, 6]]
    assert transpose(m) == transpose_zip(m) == [[1, 4], [2, 5], [3, 6]]
    assert transpose([]) == []
    assert transpose_in_place([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert transpose(transpose(m)) == m


if __name__ == "__main__":
    for row in transpose([[1, 2, 3], [4, 5, 6]]):
        print(row)
    test()
    print("All tests passed")
