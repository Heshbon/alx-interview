#!/usr/bin/python3
"""Class method for pascal triangle"""

def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    triangle = []
    if n < 1 or not isinstance(n, int):
        return triangle
    for a in range(n):
        row = []
        for b in range(a + 1):
            if b == 0 or b == a:
                row.append(1)
            elif a > 0 and b > 0:
                row.append(triangle[a - 1][b - 1] + triangle[a - 1][b])
        triangle.append(row)
    return triangle
