# HackerRank - 30 Days of Code (Day 12)

""" Inheritance """


class Person:

    def __init__(self, first_name, last_name, identifier):
        self.first_name = first_name
        self.last_name = last_name
        self.identifier = identifier

    def print_person(self):
        print("Name:", self.last_name + ",", self.first_name)
        print("ID:", self.identifier)


class Student(Person):

    def __init__(self, first_name, last_name, identifier, scores):
        Person.__init__(self, first_name, last_name, identifier)
        self.scores = scores

    def grade(self):
        total = sum(self.scores)
        average = total / len(self.scores)
        if 90 <= average <= 100:
            return 'O'
        elif 80 <= average:
            return 'E'
        elif 70 <= average:
            return 'A'
        elif 55 <= average:
            return 'P'
        elif 40 <= average:
            return 'D'
        else:
            return 'T'


if __name__ == '__main__':
    line = input().split()
    first_name = line[0]
    last_name = line[1]
    identifier = line[2]
    scores = list(map(int, input().split()))
    s = Student(first_name, last_name, identifier, scores)
    s.print_person()
    print("Grade:", s.grade())
