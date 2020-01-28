# Sodoku - Backtracking Algorithm

from timeit import default_timer as timer


def print_sodoku_board(board):
    """
        print sodoku matrix
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
        solve sodoku board using Backtracking.
        sets initial values for recursive utility function
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
        recursive function for solving
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
        [0, 4, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 6, 7, 3, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 9, 0, 1, 0],
        [0, 0, 0, 0, 6, 0, 4, 0, 0],
        [4, 0, 0, 0, 1, 5, 0, 0, 7],
        [0, 3, 0, 0, 0, 2, 0, 9, 6],
        [0, 0, 9, 0, 7, 0, 0, 0, 2],
        [0, 1, 0, 0, 0, 6, 7, 0, 4]
    ]

    start = timer()
    solve_sodoku(b)
    end = timer()
    print('\ncompleted in {} seconds'.format(end - start))
