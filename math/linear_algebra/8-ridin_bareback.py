#!/usr/bin/env python3
"""write a function that performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """returns the result of the two matrices being multiplied together"""
    if len(mat1[0]) != len(mat2):
        return None
    
    rows_mat1 = len(mat1)
    cols_mat1 = len(mat1[0])
    cols_mat2 = len(mat2[0])

    result_matrix = [[0 for _ in range(cols_mat2)] 
                     for _ in range(rows_mat1)]
    for i in range(rows_mat1):
        for j in range(cols_mat2):
            for k in range(cols_mat1):
                result_matrix[i][j] += mat1[i][k] * mat2[k][j]
    return result_matrix
