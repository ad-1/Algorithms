# HackerRank - 30 Days of Code (Day 3)

""" Class vs. Instance """


class Person:

    def __init__(self, initial_age):
        if initial_age < 0:
            print('Age is not valid, setting age to 0.')
            self.age = 0
        else:
            self.age = initial_age

    def year_pass(self):
        self.age += 1

    def am_i_old(self):
        if self.age < 13:
            print('You are young.')
        elif 13 <= self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')


# Program driver
if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        age = int(input())
        p = Person(age)
        p.am_i_old()
        for j in range(0, 3):
            p.year_pass()
        p.am_i_old()
        print("")
