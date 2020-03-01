# Bell Numbers - Dynamic Programming

"""
    Bell numbers count the possible partitions of a set.
    example set {1, 2} -> possible partitions { {1}, {2} }, { {1, 2} }
    Bell number = 2
"""


def bell(n):
    p = [set([i for i in range(1, n + 1)])]
    count = 0
    for i in range(1, n + 1):
        s = set()
        for j in range(1, i + 1):
            if i != j:
                s.add(j)
        p.append(s)
        print(p)
        count += 1


if __name__ == '__main__':
    n_ = 4
    bell(n_)
