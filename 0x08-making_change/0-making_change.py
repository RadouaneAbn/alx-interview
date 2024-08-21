#!/usr/bin/python3
""" making_change script """


def makeChange(coins, total):
    """ This function determines the fewest number of coins needed to meet
        a given amount 'total' """
    coins = list(sorted(coins, reverse=True))
    coins_count = 0
    number_of_coins = len(coins)
    i = 0
    if not coins or not total:
        return 0
    while coins and i < number_of_coins:
        coin = coins[i]
        if coin > total or coin == 0:
            i += 1
            continue
        total -= coin
        coins_count += 1
    if total == 0:
        return coins_count
    else:
        return -1
