# Fixed Point Iteration - Numerical Analysis

"""
    Method of computing fixed points of iterated functions.
    x = g(x0) => fixed points (input = output)
"""


def fixed_point_iteration(p0, tol, n):
    """
    fixed point iteration algorithm for root finding
    param p0: initial guess for root
    param n: max number of iterations
    param tol: tolerance for root approximation
    """
    i = 0
    while i < n:
        # divergent: p = (p0 ** 2) - 1  # g(p0), g(x) = x**2 - 1
        # division by zero : p = 1/(p0 - 1)
        p = 1 + 1/p0
        if abs(p - p0) < tol:
            break
        i += 1
        p0 = p
    print('root approximation = {}'.format(p))


# Program driver
if __name__ == '__main__':
    # x**2 - x - 1 = 0
    p0 = 1
    tol = 0.0001
    n = 20
    fixed_point_iteration(p0, tol, n)
