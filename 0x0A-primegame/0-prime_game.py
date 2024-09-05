#!/usr/bin/python3
""" The Prime Game Module
"""


def is_multiple(n, m):
    """ This function return true if n is not a multiple of m """
    return n % m != 0


def is_prime(n):
    """ This function checks if number is prime"""
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def get_prime(nums):
    """ This function return a prime number from a list if found """
    for n in nums:
        if is_prime(n):
            return (n)
    return None


def isWinner(x, nums):
    """ This function gets teh winner of the prime game game """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    score = {"maria": 0, "ben": 0}
    i = 0
    while i < x:
        new_list = [n for n in range(1, nums[i] + 1)]
        turn = "maria"
        while new_list:
            # print("before:", new_list)
            n = get_prime(new_list)
            turn = "ben" if turn == "maria" else "maria"
            if not n:
                break
            # print("prime found:", n)
            new_list = list(filter(lambda x: is_multiple(x, n), new_list))
            # print("after:", new_list)
        # turn = "ben" if turn == "maria" else "maria"
        score[turn] += 1
        # print(score)
        i += 1
    if score["ben"] > score["maria"]:
        return "ben"
    elif score["maria"] > score["ben"]:
        return "maria"
    else:
        return None
