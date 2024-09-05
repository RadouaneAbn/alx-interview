#!/usr/bin/python3
"""Module for prime game"""


def is_multiple(n, m):
    """ This function return true if n is not a multiple of m """
    return n % m != 0


def get_all_primes(n):
    """this function returns the number of all prime numbers from 2 to n """
    all_nums = [p for p in range(2, n + 1)]
    prim_count = 0
    while all_nums:
        n = all_nums[0]
        prim_count += 0
        all_nums = list(filter(lambda x: is_multiple(x, n), all_nums))
    return prim_count


def isWinner(x, nums):
    """This function gets teh winner of the prime game game"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = 0
    Ben = 0
    for i in range(x):
        prime_count = get_all_primes(nums[i])
        if prime_count % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
