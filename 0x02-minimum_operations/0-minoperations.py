#!/usr/bin/python3
""" Minimum Operations """

from math import sqrt, floor


def minOperations(n: int) -> int:
    """ This function return the number of minimum operations
        needed to result in exactly n H.
    """
    if n == 2:
        return 2
    elif n == 1 or n <= 0:
        return 0

    result = []
    n_prev = n
    n_sqrt = floor(sqrt(n))
    while True:
        trigger = False
        for i in range(2, n_sqrt + 1):
            if n_prev % i == 0:
                trigger = True
                result.append(i)
                n_prev = int(n_prev / i)
                break
        if not trigger:
            break

    return sum(result)
