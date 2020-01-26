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


def can_put_queen(row, col, a, b):
    """
        check if queen is in row, col or
        either diagonal
    """

    if 1 in row or 1 in col or 1 in a or 1 in b:
        return False
    return True


def is_safe(board, r, c):
    """
        check if row and column number are
         valid indexes for N*N board
    """

    if 0 <= r < len(board) and 0 <= c < len(board):
        return True
    return False


def get_indexes(board):
    """
        return all zero index paths on board
    """

    indexes = []
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            indexes.append([row_index, col_index])
    return indexes


def get_col(board, c):
    """
        get column for given column number
    """

    col = []
    for r in board:
        col.append(r[c])
    return col


def get_diagonals(board, r, c):
    """
        get the diagonal of the matrix
    """

    diagonal_a, diagonal_b = [], []
    m_c = 0
    for i in range(0, 2):
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


def get_attacking_arrs(board, r, c):
    """
        get diagonals for given row and column position
    """

    diag_a, diag_b = get_diagonals(board, r, c)
    col = get_col(board, c)
    return diag_a, diag_b, col


def valid_queen(board, r, c, row, col, a, b):
    """
        check all conditions are ok to enter queen
    """

    if is_safe(board, r, c) and can_put_queen(row, col, a, b):
        return True
    return False


def n_queen(n):
    """
        main driver method to solve n queen problem.
        sets initial values required by the
        recursive solver method
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
        problem which uses backtracking
    """

    if len(queen_pos) == len(board):
        return True

    for r in range(c_row, n):
        row = board[r]
        for c in range(0, n):
            diagonal_a, diagonal_b, col = get_attacking_arrs(board, r, c)
            if valid_queen(board, r, c, row, col, diagonal_a, diagonal_b):
                board[r][c] = 1
                queen_pos.append([r, c])
                c_row = r + 1
                if solve_n_queen(board, n, queen_pos, c_row):
                    return True
                board[queen_pos[-1][0]][queen_pos[-1][1]] = 0
                c_row = queen_pos[-1][0]
                del queen_pos[-1]

    return False


if __name__ == '__main__':
    start = timer()
    n_queen(n=10)
    end = timer()
    print('\ncompleted in {} seconds'.format(end - start))
