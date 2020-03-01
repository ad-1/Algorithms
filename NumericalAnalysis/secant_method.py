# Secant Method - Numerical Analysis

"""
    The Secant Method is second best to Newton’s Method,
    and is used when a faster convergence than Bisection
    is desired, but it is too difficult or impossible to
    take an analytical derivative of the function f(x).
"""

from sympy import *


def secant_method(y, xn_1, xn_2):
    fxn_1 = y.subs(x, xn_1)
    fxn_2 = y.subs(x, xn_2)
    xn = xn_1 - fxn_1 * ((xn_1 - xn_2) / (fxn_1 - fxn_2))
    if -0.0001 < fxn_2 < 0.0001:
        print(N(xn))
        return
    secant_method(y, xn_2, xn)


if __name__ == '__main__':
    x = symbols('x')
    y = cos(x) + 2 * sin(x) + x**2
    x0 = 0
    x1 = -0.1
    secant_method(y, x0, x1)
