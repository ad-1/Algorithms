# Fibonacci Numbers - Dynamic Programming

"""
    Find the nth fibonacci number.
    The Fibonacci sequence is the sum of the two preceding numbers, starting from 0 and 1.
"""


def fib(n):
    """ Basic """

    if n == 1 or n == 2:
        fn = 1
    else:
        fn = fib(n - 1) + fib(n - 2)
    return fn


def fib_mz(n, memo):
    """ Memoize """

    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    fn = fib_mz(n-1, memo) + fib_mz(n-2, memo)
    memo[n] = fn
    return fn


def fib_bu(n):
    """ Bottom-up """

    a, b = 0, 1
    if n == 1 or n == 2:
        return 1
    for i in range(n):
        a, b = b, a + b
    return b


# program driver
if __name__ == '__main__':

    n_ = 10
    print(fib_bu(n_))
