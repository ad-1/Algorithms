# Knight's Tour Problem - Backtracking Algorithm

"""
    A knight's tour is a sequence of moves of a
    knight on an N*N chessboard such that the
    knight visits every square only once.
"""


def is_safe(board, n, r, c):
    """
        check if (r,c) are valid indexes for board
    """

    if 0 <= r < n and 0 <= c < n and board[r][c] == -1:
        return True
    return False


def print_board(board):
    """
        print board matrix
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


def knights_tour(n):
    """
        driver method for Knight Tour problem
        which sets initial values
    """

    board = [[-1 for i in range(n)] for i in range(n)]
    print_board(board)

    mv_r = [2, 1, -1, -2, -2, -1, 1, 2]
    mv_c = [1, 2, 2, 1, -1, -2, -2, -1]

    board[0][0] = 0

    pos = 1

    if not solve_knights_tour(board, n, 0, 0, mv_r, mv_c, pos):
        print("Solution does not exist")
    else:
        print_board(board)


def solve_knights_tour(board, n, c_row, c_col, mv_r, mv_c, pos):
    """
        recursive function to solve knights tour
        using backtracking
    """

    if pos == n ** 2:
        return True

    for i in range(n):
        new_r = c_row + mv_r[i]
        new_c = c_col + mv_c[i]
        if is_safe(board, n, new_r, new_c):
            board[new_r][new_c] = pos
            if solve_knights_tour(board, n, new_r, new_c, mv_r, mv_c, pos + 1):
                return True
            board[new_r][new_c] = -1
    return False


# Driver program to test above function
if __name__ == "__main__":
    knights_tour(n=8)
