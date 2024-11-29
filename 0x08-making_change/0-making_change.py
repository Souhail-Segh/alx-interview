#!/usr/bin/python3
"""
Change coins algorithm
"""


def makeChange(coins, total):
    """ Calculate the minimal number of operation
    needed to give all the change, if failed -1
    """
    coins.sort(reverse=True)
    i = 0
    number_of_coins = -1
    max_coins = len(coins)

    while (total > 0 and i < max_coins):
        coin = coins[i]
        t_modulo = total % coin
        if t_modulo != total:
            number_of_coins = number_of_coins + total // coin
            total = t_modulo
        if t_modulo == 0:
            return (number_of_coins + 1)
        i += 1

    return (-1)
