#!/usr/bin/env python3
"""write a function that adds two arrays element-wise"""


def add_arrays(arr1, arr2):
    """returns the addition of two arrays"""
    if len(arr1) != len(arr2):
        return None

    result_matrix = []
    for i in range(len(arr1)):
        result_matrix.append(arr1[i] + arr2[i])
    return result_matrix
