#!/usr/bin/env python3
"""write a function that concats two arrays"""


def cat_arrays(arr1, arr2):
    """returns the two arrays concatenated as a new array"""
    result_array = []
    for i in range(len(arr1)):
        result_array.append(arr1[i])
    for j in range(len(arr2)):
        result_array.append(arr2[j])
    return result_array
