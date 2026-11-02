"""
PASCAL'S TRIANGLE
Meaning : Each number is the sum of the two numbers above it.
          [1] / [1,1] / [1,2,1] / [1,3,3,1] ...

Time O(n^2).  Row k is also the binomial coefficients C(k, 0..k).

Interview tips
  - Build row by row using the previous row.
  - Printing it centered is a common "pattern" question - see print_triangle.
"""


def pascal_triangle(rows):
    tri = []
    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = tri[i - 1][j - 1] + tri[i - 1][j]
        tri.append(row)
    return tri


def print_triangle(rows):
    tri = pascal_triangle(rows)
    width = len(" ".join(map(str, tri[-1])))
    for row in tri:
        print(" ".join(map(str, row)).center(width))


def test():
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert pascal_triangle(0) == []


if __name__ == "__main__":
    print_triangle(6)
    test()
    print("All tests passed")
