#!/usr/bin/python3
""" Good Problem """


def makeChange(coins, total):
    """
        determine the fewest number of coins needed to meet a
        given amount total
    """
    if total <= 0:
        return 0
    coins = sorted(coins)
    ans = 0
    for i in range(len(coins) - 1, -1, -1):
        if total >= coins[i]:
            count = int(total / coins[i])
            ans += count
            total -= (coins[i] * count)
    if total == 0:
        return ans
    else:
        return -1
