"""

A string is said to be a special string if either of two conditions is met:

- All of the characters are the same, e.g. aaa.
- All characters except the middle one are the same, e.g. aadaa.

Given a string, determine how many special substrings can be formed from it.

"""


# def substr_count(n, s):
#     tot = 0
#     count_sequence = 0
#     prev = ''
#     for i, v in enumerate(s):
#         count_sequence += 1
#         if i and (prev != v):
#             j = 1
#             while ((i-j) >= 0) and ((i+j) < len(s)) and j <= count_sequence:
#                 if s[i-j] == prev == s[i+j]:
#                     tot += 1
#                     j += 1
#                 else:
#                     break
#             count_sequence = 1
#         tot += count_sequence
#         prev = v
#     return tot

import copy


# def substr_count(n, s):
#     if n < 1 or n > 10000000:
#         return 0
#     count = 0
#     char_count = {}
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1
#     exc_i = None
#     exc_j = None
#     for i in range(0, n):
#         char_count_i = char_count.copy()
#         if i != 0 and exc_i is not None:
#             char_count_i[exc_i] -= 1
#             if char_count_i[exc_i] <= 0:
#                 char_count_i.pop(exc_i, None)
#         for j in range(n, i, -1):
#             perm = s[i:j]
#             n_perm = j - i
#             if j != len(s) and exc_j is not None:
#                 char_count_i[exc_j] -= 1
#                 if char_count_i[exc_j] <= 0:
#                     char_count_i.pop(exc_j, None)
#             if n_perm % 2 != 0:
#                 if char_count_i[perm[0]] == n_perm - 1 and perm[(n_perm // 2) + 1] != perm[0]:
#                     count += 1
#                     j = n_perm // 2
#                 elif char_count_i[perm[0]] == n_perm:
#                     count += 1
#             elif char_count_i[perm[0]] == n_perm:
#                 count += 1
#             exc_j = perm[-1]
#         exc_i = exc_j
#     return count

if __name__ == '__main__':
    _s = 'aaaa'
    _n = len(_s)
    print(substr_count(_n, _s))
