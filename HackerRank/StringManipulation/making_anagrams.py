"""

HackerRank: String Manipulation
    We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string.

    For example, bacdc and dcbac are anagrams

    Given two strings, a and b, that may or may not be of the same length,
    determine the minimum number of character deletions required to make
    a and b anagrams. Any characters can be deleted from either of the strings.

"""


def make_anagram(_a, _b):
    hash_a = {}
    hash_b = {}
    for char in _a:
        hash_a[char] = hash_a.get(char, 0) + 1
    for char in _b:
        hash_b[char] = hash_b.get(char, 0) + 1
    num_deletions = 0
    for k in hash_a.keys():
        if k not in hash_b:
            num_deletions += hash_a[k]
    for k in hash_b.keys():
        if k not in hash_a:
            num_deletions += hash_b[k]
        elif hash_b[k] != hash_a[k]:
            num_deletions += abs(hash_b[k] - hash_a[k])
    return num_deletions


if __name__ == '__main__':
    a = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
    b = "fcrxzwscanmligyxyvym"  # input()
    res = make_anagram(a, b)
    print(res)
