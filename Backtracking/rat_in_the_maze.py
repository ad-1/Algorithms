# Rat in the Maze - Backtracking Algorithm

"""
    In this problem, there is a given maze of size N x N.
    The source and the destination location is top-left
    cell and bottom right cell respectively.
    The objective is the find the path from the source
    to the destination if one exists.
"""

from timeit import default_timer as timer


def print_maze(maze, n):
    """
        print maze matrix
    """

    print()
    for i in range(n):
        for j in range(n):
            print(maze[i][j], end=' ')
        print()
    print()


def is_in_maze(x, y, n):
    """
        check x,y coordinates are in the maze
    """

    if 0 <= x < n and 0 <= y < n:
        return True
    return False


def can_move_forward(r, c, maze):
    """
        check if the path is clear
    """

    if maze[r][c] == 0:
        return False
    return True


def can_proceed_through_maze(r, c, n, maze, visited):
    """
        check all conditions are valid to proceed
        to next row and column in maze
    """
    if is_in_maze(r, c, n) \
            and can_move_forward(r, c, maze) \
            and not any(([r, c]) in visited for p in visited):
        return True
    return False


def rat_in_maze():
    """
        Main driver method to set initial values
        for solving maze problem.
        Prints solution matrix if solvable.
    """

    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]

    # maze = [[1, 0, 1, 1, 1, 1, 0],
    #         [1, 0, 1, 0, 1, 0, 1],
    #         [1, 1, 1, 1, 0, 0, 1],
    #         [0, 0, 1, 0, 1, 1, 1],
    #         [0, 1, 1, 1, 1, 0, 1],
    #         [0, 1, 0, 0, 0, 0, 1],
    #         [1, 1, 0, 0, 0, 0, 1]]

    n = len(maze)
    path = [[0 for i in range(n)] for i in range(n)]
    print_maze(maze, n)

    r = 0
    c = 0

    path[r][c] = 1

    mv_r = [0, 1, 0, -1]  # move up and down
    mv_c = [1, 0, -1, 0]  # move left and right

    visited = [[r, c]]

    if not solve_maze(maze, path, n, r, c, mv_r, mv_c, visited):
        print("Solution does not exist")
    else:
        print_maze(path, n)


def solve_maze(maze, path, n, r, c, mv_r, mv_c, visited):
    """
        main recursive method to solve the rat
        in the maze problem using backtracking
    """

    if r == c == n - 1:
        return True

    for i in range(len(mv_r)):
        new_row = r + mv_r[i]
        new_col = c + mv_c[i]
        if can_proceed_through_maze(new_row, new_col, n, maze, visited):
            path[new_row][new_col] = 1
            visited.append([new_row, new_col])
            if solve_maze(maze, path, n, new_row, new_col, mv_r, mv_c, visited):
                return True
            path[new_row][new_col] = 0
    return False


# Driver program to test above function
if __name__ == "__main__":
    start = timer()
    rat_in_maze()
    end = timer()
    print('\ncompleted in {} seconds'.format(end - start))
