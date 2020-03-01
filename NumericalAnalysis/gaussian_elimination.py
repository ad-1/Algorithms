# Gaussian Elimination - Numerical Analysis

"""
    Gaussian elimination algorithm used to solve
    systems of linear equations
"""

import sympy as sp
import numpy as np

x1, x2, x3 = sp.symbols('x1 x2 x3')


def equations():

    eq1 = -3 * x1 + 2 * x2 - x3 + 1
    eq2 = 6 * x1 - 6 * x2 + 7 * x3 + 7
    eq3 = 3 * x1 - 4 * x2 + 4 * x3 + 6

    # eq1 = x1 - 2 * x2 - x3 - 6
    # eq2 = 2 * x1 + 2 * x2 - x3 - 1
    # eq3 = -x1 - x2 + 2 * x3 - 1

    return [eq1, eq2, eq3]


def matrix_representation(system):
    a, b = sp.linear_eq_to_matrix(system, [x1, x2, x3])
    m = a.col_insert(3, b)
    return m


def elimination(m):
    """
        Allowed operations are:
            (1) multiply any row by a constant
            (2) add multiple of one row to another row
            (3) inter- change the order of any rows
        objective: convert matrix into an upper-triangular matrix
    """

    shape = m.shape
    nrows, ncols = shape[0], shape[1]
    for i, row in enumerate(m):
        j, v = next((j, elem) for (j, elem) in enumerate(row) if elem != 0)
        m[i] = row / v
        for rr in range(i + 1, nrows):
            m[rr] = m[rr] - m[i] * m[rr][j]
    return m


def backsubstitution(m):
    syms = [x1, x2, x3]
    ctr = len(syms) - 1
    for row in reversed(m):
        eqn = syms[0] * row[0] + syms[1] * row[1] + syms[2] * row[2] - row[3]
        syms[ctr] = sp.solve(eqn, syms[ctr])[0]
        ctr -= 1
    return syms


def validate_solution(system, x_1, x_2, x_3):
    print('\nvalidation')
    for eqn in system:
        print(eqn.subs([(x1, x_1), (x2, x_2), (x3, x_3)]))


def linalg_test():
    system = equations()
    M, c = sp.linear_eq_to_matrix(system, [x1, x2, x3])
    M, c = np.asarray(M, dtype=np.float32), np.asarray(c, dtype=np.float32)
    y = np.linalg.solve(M, c)
    print('\nsolutions')
    print(y)


if __name__ == '__main__':
    eqns = equations()
    [print(eqn) for eqn in eqns]
    M = np.asarray(matrix_representation(eqns), dtype=np.float32)
    ref = elimination(M)
    sol = backsubstitution(ref)
    sp.pprint('\nx1 = {:.2f}\nx2 = {:.2f}\nx3 = {:.2f}'.format(sol[0], sol[1], sol[2]))
    validate_solution(eqns, sol[0], sol[1], sol[2])
    linalg_test()
