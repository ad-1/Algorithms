# HackerRank - 30 Days of Code (Day 7)


def tests():
    txt = " apple, banana, cherry "
    test_rsplit(txt)
    test_rstrip(txt)


def test_rsplit(txt):
    # setting the maxsplit parameter to 1, returns a list with 2 elements
    x = txt.rsplit(", ", 1)
    print('rsplit:', x, 'len:', len(x), type(x))


def test_rstrip(txt):
    # rstrip method returns a copy of a string with trailing chars removed
    x = txt.rstrip()
    print('rstrip:', x, 'len:', len(x), type(x))


# Program driver
if __name__ == '__main__':
    # tests()
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    for i in reversed(arr):
        print(i, end=' ')
    print()
