# HackerRank - 30 Days of Code (Day 6)

""" Let's review """


def print_even_odd_words(word):
    """
    print even and odd letters in a string
    """
    even, odd = [], []
    for i, letter in enumerate(word):
        if i % 2 == 0:
            even.append(letter)
        else:
            odd.append(letter)
    print(''.join(even), ''.join(odd))


# Program driver
if __name__ == '__main__':
    n = int(input())  # input number of test cases
    for i in range(0, n):
        word = input()  # read word
        print_even_odd_words(word)
