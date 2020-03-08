# Bisection Method - Numerical Analysis

import math

"""
    The bisection method is a root-finding method
    that applies to any continuous functions
    for which one knows two values with opposite signs.

    (related to Intermediate Value Theorem)

    If there is a root of f(x) on the interval [a, b]
    then f(a) and f(b) must have a difference sign.
    i.e. f(a)f(b) < 0

"""


def f(x):
    y = x ** 3 + 4 * x ** 2 - 10
    return y


def check_root_bracket(x0, x1):
    """
    check interval can be used to solve for root
    """
    f_x1 = f(x0)
    f_x2 = f(x1)
    if f_x1 * f_x2 < 0:
        return True
    return False


def bisection(n, interval, err):
    """
    solve for root using bisection method
    """
    x0, x1 = interval[0], interval[1]
    if not check_root_bracket(x0, x1):
        return None
    for i in range(n):
        x2 = x0 + ((x1 - x0) / 2)
        y = f(x2)
        if -err < y < err:
            return x2
        if check_root_bracket(x0, x2):
            x1 = x2
        else:
            x0 = x2
    return None


def error_bound(interval, err):
    """
    determine the number of iterations required to find the
    root within a specified error bound
    """
    # err = (b-a)/(2**n) # == abs(root_approx - root)
    # err(2**n) = (b-a)
    # 2**n = (b-a)/err
    # ln(2**n) = ln((b-a)/err)
    # nln(2) = ln((b-a)/err)
    a, b = interval[0], interval[1]
    n = math.log((b-a)/(math.log(2)*err))
    return int(math.ceil(n))


# Program driver
if __name__ == '__main__':
    a_b = [1, 2]
    _err = 0.0001
    n_approx = error_bound(a_b, _err)
    print('Number of iterations error bound: {}'.format(n_approx))
    root = bisection(n_approx, a_b, _err)
    if root:
        print('root of f(x) on interval {} : x = {}'.format(a_b, root))
    else:
        print('Bisection method failed')
