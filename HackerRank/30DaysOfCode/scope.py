# HackerRank - 30 Days of Code (Day 14)

""" Scope """


class Difference:

    def __init__(self, a):
        self.__elements = a
        self.maximum_difference = 0

    def compute_difference(self):
        min_value = min(self.__elements)
        max_value = max(self.__elements)
        self.maximum_difference = max_value - min_value


if __name__ == '__main__':
    _ = input()
    a = [int(e) for e in input().split(' ')]
    d = Difference(a)
    d.compute_difference()

    print(d.maximum_difference)
