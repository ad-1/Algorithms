# Knight's Tour Problem - Backtracking Algorithm

n = 8


def is_safe(board, row, col):
    """
        check if i,j are valid indexes for N*N chessboard
    """

    if 0 <= row < n and 0 <= col < n and board[row][col] == -1:
        return True
    return False


def print_board(board):
    """
        print board matrix
    """

    print()
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=' ')
        print()


def solve_knights_tour():
    """
        solver driver method Knight Tour problem
    """

    board = [[-1 for i in range(n)] for i in range(n)]
    print_board(board)

    # move_x and move_y define next move of Knight
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Since the Knight is initially at the first block
    board[0][0] = 0

    # Step counter for knight's position
    pos = 1

    if not solve_knights_tour_util(board, 0, 0, move_x, move_y, pos):
        print("Solution does not exist")
    else:
        print_board(board)


def solve_knights_tour_util(board, curr_x, curr_y, move_x, move_y, pos):
    """
        recursive function
    """

    if pos == n ** 2:
        return True

    for i in range(n):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if is_safe(new_x, new_y, board):
            board[new_x][new_y] = pos
            if solve_knights_tour_util(board, new_x, new_y, move_x, move_y, pos + 1):
                return True
            board[new_x][new_y] = -1
    return False


# Driver program to test above function
if __name__ == "__main__":
    solve_knights_tour()
