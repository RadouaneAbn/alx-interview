#!/usr/bin/python3

def pascal_triangle(num):
    if type(num) is not int:
        raise TypeError("The input should be a number")
    if num <= 0:
        return []
    result = [[1]]
    for i in range(1, num):
        prev = i - 1
        sub_result = []
        for j in range(0, i + 1):
            sub_result.append(
                (j > 0 and result[prev][j - 1]) + (j < i and result[prev][j])
            )
        result.append(sub_result)

    return result
