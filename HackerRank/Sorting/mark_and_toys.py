"""

Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy?

For example, if prices = [1, 2, 3, 4] and Mark has k = 7 to spend he can buy [1, 2, 3] or [3, 4].
He would choose the first group of 3 items.

A toy can't be bought multiple times.

prices = array of toy prices
k = budget

"""


def maximum_toys(prices, k):
    prices.sort()
    i = 0
    toys = 0
    spent = 0
    while True:
        spent += prices[i]
        if spent >= k:
            break
        toys += 1
        i += 1
    return toys


if __name__ == "__main__":
    _prices = [1, 12, 5, 111, 200, 1000, 10]
    _k = 50
    result = maximum_toys(_prices, _k)
    print(result)
