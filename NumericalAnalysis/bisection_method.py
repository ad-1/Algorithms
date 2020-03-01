# Bisection Method - Numerical Analysis

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
    f_x1 = f(x0)
    f_x2 = f(x1)
    if f_x1 * f_x2 < 0:
        return True
    return False


def bisection(n, interval):
    x0, x1 = interval[0], interval[1]
    if not check_root_bracket(x0, x1):
        return None
    for i in range(n):
        x2 = x0 + ((x1 - x0) / 2)
        y = f(x2)
        if -0.0001 < y < 0.0001:
            return x2
        if check_root_bracket(x0, x2):
            x1 = x2
        else:
            x0 = x2
    return None


if __name__ == '__main__':

    n_iter = 100
    a_b = [1, 2]
    root = bisection(n_iter, a_b)
    if root:
        print('root of f(x) on interval {} : x = {}'.format(a_b, root))
    else:
        print('Bisection method failed')
