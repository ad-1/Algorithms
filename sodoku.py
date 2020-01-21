# Backtracking algorithm - sodoku solver

import itertools as it


def print_sodoku_board(board):
    """
        A utility function to print matrix
    """

    print()
    n = len(board)
    for i in range(n):
        for j in range(n):
            if len(str(board[i][j])) == 2:
                print('{}'.format(board[i][j]), end=' ')
            else:
                print(' {}'.format(board[i][j]), end=' ')
        print()


def is_on_board(zero, board):
    """
    check if i,j are valid indexes for N*N board
    """

    n = len(board)
    if n > zero[0] >= 0 and 0 <= zero[1] < n:
        return True
    return False


def get_zeros(board):
    """
    return all zero index paths on board
    """

    zeros = []
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if board[row_index][col_index] == 0:
                zeros.append([row_index, col_index])
    return zeros


def get_row_and_col(board, zero):
    """
    get row and column for zero
    """

    row = board[zero[0]]
    c = zero[1]
    col = []
    for r in board:
        col.append(r[c])
    return row, col


def validate_entry(board, zero, val, grid_size):
    """
    validate value is a possible solution in given row, column and grid
    """

    row, col = get_row_and_col(board, zero)
    if val in row or val in col:
        return False

    grid_x = zero[1] // grid_size
    grid_y = zero[0] // grid_size

    for i in range(grid_y * grid_size, (grid_y * grid_size) + grid_size):
        for j in range(grid_x * grid_size, (grid_x * grid_size) + grid_size):
            if board[i][j] == val and (i, j) != zero:
                return False

    return True


def solve_sodoku(board):
    """
        This function solves sodoku board using Backtracking. This function mainly uses solve_sokodu_util()
        to solve the problem. It returns false if no complete board is possible, otherwise return true and prints the
        solution board. Please note that there may be more than one solution,
        this function prints one of the feasible solutions.
    """

    print_sodoku_board(board)
    zeros = get_zeros(board)
    grid_size = int(len(board) ** (1 / 2))

    if not solve_sokodu_util(board, zeros, 0, grid_size):
        print("Solution does not exist")
    else:
        print_sodoku_board(board)


def solve_sokodu_util(board, zeros, pos, grid_size):
    """
     A recursive utility function to solve sodoku problem using backtracking
    """

    if not any(0 in row for row in board):
        return True

    zero = zeros[pos]

    for val in range(1, len(board) + 1):
        if validate_entry(board, zero, val, grid_size):
            board[zero[0]][zero[1]] = val
            pos += 1
            if solve_sokodu_util(board, zeros, pos, grid_size):
                return True

            board[zero[0]][zero[1]] = 0
            pos -= 1

    return False


# Driver program to test above function
if __name__ == "__main__":

    b = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    solve_sodoku(b)
