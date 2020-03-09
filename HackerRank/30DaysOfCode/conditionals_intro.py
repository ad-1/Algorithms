# HackerRank - 30 Days of Code (Day 3)

""" Into to conditional statements """

n = int(input())

mod = n % 2

if mod != 0 or (mod == 0 and 6 <= n <= 20):
    print('Weird')
elif (mod == 0 and 2 <= n <= 5) or (mod == 0 and n > 20):
    print('Not Weird')
