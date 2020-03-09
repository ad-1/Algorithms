# HackerRank - 30 Days of Code (Day 8)

""" Dictionaries and Maps """

import sys


if __name__ == '__main__':

    phone_book = {}
    n = int(input().strip())
    entries = []

    for i in range(0, n):
        entry = input().split()
        if len(entry) > 2:
            continue
        phone_book[entry[0]] = entry[1]

    query = sys.stdin.readline().strip()
    while query:
        number = phone_book.get(query)
        if number:
            print('{}={}'.format(query, number))
        else:
            print('Not found')
        query = sys.stdin.readline().strip()
