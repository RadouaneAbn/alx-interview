#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n):
    """ This function return a list of lists representing
        Pascla's triangle of a number n
    """
    if type(n) is not int:
        raise TypeError("The input should be a number")
    if n <= 0:
        return []
    result = [[1]]
    for i in range(1, n):
        prev = i - 1
        result.append([
            (j > 0 and result[prev][j - 1]) + (j < i and result[prev][j])
            for j in range(0, i + 1)
            ])

    return result
