"""
HackerRank String Manipulation

You are given a string containing characters A and B.

Your task is to change it into a string such that there are no matching adjacent characters.
To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.
"""


def alternating_characters(s):
    res = [s[0]]
    for i in range(0, len(s) - 1):
        if s[i] != s[i + 1]:
            res.append(s[i + 1])
    return len(s) - len(res)


if __name__ == '__main__':

    s = 'AAABBB'
    alternating_characters(s)
