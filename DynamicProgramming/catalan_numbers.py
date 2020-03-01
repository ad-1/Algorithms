# Catalan Numbers - Dynamic Programming

"""
    Catalan numbers form a sequence of natural numbers that occur
    in various counting problems, often involving recursively-defined objects
"""

from timeit import default_timer as timer


def factorial(n, _):
    """
        n factorial function using ternary operator
        or for loop
    """
    # return 1 if n == 0 or n == 1 else n * _factorial(n - 1)

    if n <= 1:
        return 1
    f = n
    for i in range(n, 1, -1):
        f = f * (i - 1)
    return f


def _factorial(n, f_memo):
    """
        n factorial using memoization.
        requires input matrix of [1, 1] otherwise
        remove comments
    """

    # if n <= 1:
    #     return 1
    if len(f_memo) > n and f_memo[n] is not None:
        return f_memo[n]
    f = n * _factorial(n - 1, f_memo)
    f_memo[n] = f
    return f


def catalan(n, f_memo):
    """ nth Catalan number is given directly in terms of binomial coefficients """

    c_n = _factorial(2 * n, f_memo) // (_factorial(n + 1, f_memo) * _factorial(n, f_memo))
    return c_n


def catalan_dp(n, c_nums):
    if len(c_nums) > n and c_nums[n] is not None:
        return c_nums[n]
    s = 0
    for i in range(n):
        s += catalan_dp(i, c_nums) * catalan_dp(n-i-1, c_nums)
    c_nums[n] = s
    return c_nums[n]


if __name__ == '__main__':

    n_ = 500

    # 1
    catalan_numbers = []
    f_memo_ = [None] * (n_ * 2)
    f_memo_[0], f_memo_[1] = 1, 1
    start = timer()
    for c in range(0, n_):
        catalan_numbers.append(catalan(c, f_memo_))
    end = timer()
    print(catalan_numbers[-1])
    print(end - start, 'seconds')

    # 2
    n_ = 499
    c_nums_ = [None for _ in range(n_ + 1)]
    c_nums_[0], c_nums_[1] = 1, 1
    start = timer()
    print(catalan_dp(n_, c_nums_))
    end = timer()
    print(end - start, 'seconds')
