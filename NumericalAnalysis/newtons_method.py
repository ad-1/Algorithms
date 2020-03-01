# Newton's Method - Numerical Analysis

"""
    Newton's root-finding algorithm for approximating
    the roots of a real-valued function.

    f(x) and f'(x) must be continuous
"""

from sympy import *


def newtons_method(y, x_0):
    dy = diff(y)
    x_n = x - (y / dy)
    x_, f_xn, df_xn = x_0, y.subs(x, x_0), dy.subs(x, x_0)
    while not -0.0001 < f_xn < 0.0001:
        xnp1 = x_n.subs([(x, x_), (y, f_xn), (dy, df_xn)])
        x_ = xnp1
        f_xn = y.subs(x, x_)
        df_xn = dy.subs(x, x_)
    return x_.evalf()


###############################################################
    # Recursive solution
###############################################################


def newtons_method_(y, x_0):
    dy = diff(y)
    x_n = x - (y / dy)
    newtons_method_recursive(x_0, x_n, y, dy)


def newtons_method_recursive(x_, x_n, y, dy):
    f_xn = y.subs(x, x_)
    if -0.0001 < f_xn.evalf() < 0.0001:
        print(N(x_))
        return
    df_xn = dy.subs(x, x_)
    xnp1 = x_n.subs([(x, x_), (y, f_xn), (dy, df_xn)])
    newtons_method_recursive(xnp1, x_n, y, dy)


if __name__ == '__main__':
    x = symbols('x')
    f_x = cos(x) - x
    x0 = 1
    newtons_method_(f_x, x0)
