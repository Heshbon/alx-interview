#!/usr/bin/python3
""" The module to rotate an n x n 2D matrix by 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """ Rotates n x n 2D matrix 90 degrees clockwise."""
    n = len(matrix)
    # Transposes the matrix
    for a in range(n):
        for b in range(a, n):
            matrix[a][b], matrix[b][a] = matrix[b][a], matrix[a][b]
    # Reverses each row
    for row in matrix:
        row.reverse()
