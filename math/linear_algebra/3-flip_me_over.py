#!/usr/bin/env python3
"""write a function the tranposes a 2D matrix"""


def matrix_transpose(matrix):
    """returns the tranpose of a 2D matrix"""
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    transposed_matrix = [[0 for _ in range(num_rows)] for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix
