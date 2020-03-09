# Hacker Rank - 30 Days of Code (Day 1)

""" Data Types """

i = 4
d = 4.0
s = 'HackerRank '

input_int = input()
input_double = input()
ss = input()

try:
    ii = int(input_int)
    dd = float(input_double)
except Exception as e:
    print(e)
    exit()

print(i + ii)
print(d + dd)
print(s + ss)
