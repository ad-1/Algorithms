# Dynamic Programming - Ugly Numbers

"""
    Given a number n, the task is to find n’th Ugly number
    Ugly numbers are numbers whose only prime factors are 2, 3 or 5

    The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers.
    By convention, 1 is included.
"""

from timeit import default_timer as timer

############################################################################
""" Ugly Numbers - Attempt """
############################################################################


def get_divisors(num):
    """ get all divisors of a number """

    divisors = [1, num]
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def is_prime_number(num):
    """ check if number is prime """

    if get_divisors(num) == [1, num]:
        return True
    return False


def is_ugly_num(num):
    """ check if number is ugly """

    sequence = [1, 2, 3, 5]
    prime_factors = []
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        divisors = get_divisors(num)
        for d in divisors:
            if d not in sequence and is_prime_number(d):
                prime_factors.append(d)
        if not prime_factors:
            return True
    return False


def nth_ugly_num(n):
    """ get nth ugly number """

    ugly_nums = [1]
    num = 2
    while len(ugly_nums) < n:
        if is_ugly_num(num):
            ugly_nums.append(num)
        num += 1
    return ugly_nums[-1]


############################################################################
""" Ugly Numbers - Brute Force """
############################################################################


def is_ugly(num):
    while True:
        if num == 1:
            return True
        if num % 2 == 0:
            num //= 2
        elif num % 3 == 0:
            num //= 3
        elif num % 5 == 0:
            num //= 5
        else:
            return False


def ugly_numbers(n):
    ugly_nums = [1]
    count = 2
    while len(ugly_nums) < n:
        if is_ugly(count):
            ugly_nums.append(count)
        count += 1
    return ugly_nums


############################################################################
""" Ugly Numbers - Dynamic Programming (Bottom-Up) """
############################################################################


def ugly_n(n):
    ugly_nums = [1]
    i2, i3, i5, = 0, 0, 0
    nm2, nm3, nm5 = 2, 3, 5
    while len(ugly_nums) < n:
        ugly = min(nm2, nm3, nm5)
        ugly_nums.append(ugly)
        if ugly == nm2:
            i2 += 1
            nm2 = ugly_nums[i2] * 2
        if ugly == nm3:
            i3 += 1
            nm3 = ugly_nums[i3] * 3
        if ugly == nm5:
            i5 += 1
            nm5 = ugly_nums[i5] * 5
    return ugly_nums


# Driver code to test above functions
if __name__ == '__main__':

    n_ = 150
    start = timer()
    uns = ugly_n(n_)
    print('{} (nth) ugly number is {}'.format(n_, uns[-1]))
    end = timer()
    print('completed in {} seconds'.format(end - start))
