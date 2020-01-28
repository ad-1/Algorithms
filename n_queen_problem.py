# N Queen Problem - Backtracking Algorithm

"""
N Queen is the problem of placing N chess queens on an N×N chessboard
No two queens attack each other
"""

from timeit import default_timer as timer


def init_board(n):
    """
        initialize nxn queen board
    """

    board = [[0 for i in range(n)] for i in range(n)]
    return board


def gen_random_matrix(n):
    """
        generate n*n matrix with random integers
        between 0 and n
    """

    from random import randrange
    matrix = [[randrange(n) for i in range(n)] for j in range(n)]
    return matrix


def print_board(board):
    """
        print board matrix
    """

    print()
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=' ')
        print()
    print()


def is_safe(board, r, c):
    """
        check if row and column position is
        valid index for N*N board
    """

    if 0 <= r < len(board) and 0 <= c < len(board):
        return True
    return False


def get_indexes(board):
    """
        return all zero positions as
        index path list on board
    """

    indexes = []
    for ir, row in enumerate(board):
        for ic, col in enumerate(row):
            indexes.append([ir, ic])
    return indexes


def get_col(board, r, c):
    """
        get column elements for given column number
    """

    col = []
    for row in board:
        col.append(row[c])
    return col


def get_diagonals(board, r, c):
    """
        get left and right diagonal elements relative
        to a given row and column position
    """

    diagonal_a, diagonal_b = [], []
    m_c = 1
    for i in range(0, 1):
        ma = [[+1, +1], [-1, -1]]
        mb = [[+1, -1], [-1, +1]]
        a = [r + 1 * ma[m_c][0], c + 1 * ma[m_c][1]]
        b = [r + 1 * mb[m_c][0], c + 1 * mb[m_c][1]]
        while is_safe(board, a[0], a[1]):
            diagonal_a.append(board[a[0]][a[1]])
            a[0] = a[0] + 1 * ma[m_c][0]
            a[1] = a[1] + 1 * ma[m_c][1]
        while is_safe(board, b[0], b[1]):
            diagonal_b.append(board[b[0]][b[1]])
            b[0] = b[0] + 1 * mb[m_c][0]
            b[1] = b[1] + 1 * mb[m_c][1]
        m_c += 1
    return diagonal_a, diagonal_b


def attacked_elements(board, r, c):
    """
        return column, and both diagonals
        which will be attacked if a queen
        is placed in r, c
    """

    a, b = get_diagonals(board, r, c)
    row = board[r]
    col = get_col(board, r, c)
    return a, b, row, col


def can_put_queen(row, col, a, b):
    """
        check if queen is in row, col or either diagonal
        a, b = diagonals for given row and column position
    """

    if 1 in row or 1 in col or 1 in a or 1 in b:
        return False
    return True


def valid_queen(board, r, c, row, col, a, b):
    """
        check all conditions are OK to input queen
        in (r, c)
    """

    if is_safe(board, r, c) and can_put_queen(row, col, a, b):
        return True
    return False


def n_queen(n):
    """
        main driver method to solve n queen problem.
        sets initial values required by the recursive method
    """

    queen_pos = []
    board = init_board(n)
    if solve_n_queen(board, n, queen_pos, 0):
        print_board(board)
    else:
        print('No solution')


def solve_n_queen(board, n, queen_pos, c_row):
    """
        recursive solve method for n queen
        problem using backtracking
    """

    if len(queen_pos) == len(board):
        return True

    for r in range(c_row, n):
        for c in range(0, n):
            diagonal_a, diagonal_b, row, col = attacked_elements(board, r, c)
            if valid_queen(board, r, c, row, col, diagonal_a, diagonal_b):
                board[r][c] = 1
                queen_pos.append([r, c])
                if solve_n_queen(board, n, queen_pos, r + 1):
                    return True
                board[queen_pos[-1][0]][queen_pos[-1][1]] = 0
                del queen_pos[-1]

    return False


if __name__ == '__main__':
    start = timer()
    n_queen(n=12)
    end = timer()
    print('\ncompleted in {} seconds'.format(end - start))
