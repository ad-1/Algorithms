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


def get_grid_info(board):
    """
    return all grids and a list of indexes within each grid on the board
    """

    grids = []
    grid_indexes = []
    n_rows, n_cols = len(board), len(board[0])
    grid_range = int(n_rows**(1/2))
    for i, j in it.product(range(0, n_rows, grid_range), range(0, n_cols, grid_range)):
        grid = []
        indexes = []
        for dj, di in it.product(range(grid_range), range(grid_range)):
            grid.append(board[i + di][j + dj])
            indexes.append([i + di, j + dj])
        grids.append(grid)
        grid_indexes.append(indexes)
    return grids, grid_indexes


def get_curr_grid(zero, grids):
    """
    get grid and grid number for zero
    """

    grid_size = int(len(grids) ** (1 / 2))
    grid_number = 0
    for r in range(grid_size):
        for c in range(grid_size):
            if r * grid_size <= zero[0] <= (r * grid_size) + (grid_size - 1) and \
                    c * grid_size <= zero[1] <= (c * grid_size) + grid_size - 1:
                return grids[grid_number], grid_number
            grid_number += 1


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


def update_grids(grids, grid_number, val):
    """
    backtrack grid value
    """

    grid = grids[grid_number]
    grid[:] = [0 if x == val else x for x in grid]
    grids[grid_number] = grid
    return grids


def validate_entry(row, col, grid, val):
    """
    validate value is a possible solution in given row, column and grid
    """

    if val in row or val in col or val in grid:
        return 0
    return val


def solve_sodoku():
    """
        This function solves sodoku board using Backtracking. This function mainly uses solve_sokodu_util()
        to solve the problem. It returns false if no complete board is possible, otherwise return true and prints the
        solution board. Please note that there may be more than one solution,
        this function prints one of the feasible solutions.
    """

    board = [
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

    print_sodoku_board(board)
    zeros = get_zeros(board)
    grids, grid_indexes = get_grid_info(board)
    values = list(range(1, len(board) + 1))
    pos = 0

    if not solve_sokodu_util(board, zeros, grids, grid_indexes, {}, pos, values):
        print("Solution does not exist")
    else:
        print_sodoku_board(board)


def solve_sokodu_util(board, zeros, grids, grid_indexes, tried, pos, values):
    """
     A recursive utility function to solve sodoku problem using backtracking
    """

    if not any(0 in row for row in board):
        return True

    zero = zeros[pos]
    row, col = get_row_and_col(board, zero)
    grid, grid_number = get_curr_grid(zero, grids)

    for val in values:
        z_key = tuple(zero)
        tried.setdefault(z_key, [])
        if not any([val in tried[z_key]]):
            tried[z_key].append(val)
            if not validate_entry(row, col, grid, val) == 0:
                board[zero[0]][zero[1]] = val
                grid_index = grid_indexes[grid_number].index(zero)
                grids[grid_number][grid_index] = val
                pos += 1
                if solve_sokodu_util(board, zeros, grids, grid_indexes, tried, pos, values):
                    return True

                # Backtracking
                grids[grid_number][grid_index] = 0
                board[zero[0]][zero[1]] = 0
                curr_zero = zeros[pos]
                tried[tuple(curr_zero)] = []
                pos -= 1

    return False


# Driver program to test above function
if __name__ == "__main__":
    solve_sodoku()
