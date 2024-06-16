#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n: int) -> int:
    """ This function return the number of minimum operations
        needed to result in exactly n H.
    """
    if n <= 1:
        return 0

    left = 2
    result = []
    while left**2 <= n:
        if n % left == 0:
            result.append(left)
            n //= left
        else:
            left += 1
    if n > 1:
        result.append(n)
    return sum(result)
