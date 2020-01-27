# Rat in the Maze - Backtracking Algorithm


def print_maze(maze, n):
    """
        print maze matrix
    """

    print()
    for i in range(n):
        for j in range(n):
            print(maze[i][j], end=' ')
        print()


def is_in_maze(x, y, n):
    """
        check x,y coordinates are in the maze
    """

    if 0 <= x < n and 0 <= y < n:
        return True
    return False


def can_move_forward(row, col, maze):
    """
        check if the path is clear and return
        True if can move forward in the maze
    """

    if maze[row][col] == 0:
        return False
    return True


def proceed_through_maze(maze, path, n, r, c, mv_r, mv_c, visited):
    """
        main recursive method to solve the rat
        in the maze problem using backtracking
    """

    if r == c == n - 1:
        return True

    for i in range(len(mv_r)):
        new_row = r + mv_r[i]
        new_col = c + mv_c[i]
        if is_in_maze(new_row, new_col, n):
            if can_move_forward(new_row, new_col, maze) and not any(([new_row, new_col]) in visited for point in visited):
                path[new_row][new_col] = 1
                visited.append([new_row, new_col])
                if proceed_through_maze(maze, path, n, new_row, new_col, mv_r, mv_c, visited):
                    return True
                path[new_row][new_col] = 0
            else:
                visited.append([new_row, new_col])
    return False


def traverse_maze():
    """
        Main driver method to set initial values
        for solving using backtracking.
        returns false if no path is possible,
        otherwise prints the solution matrix.
    """

    maze = [[1, 0, 1, 1, 1, 1, 0],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 1, 0, 0, 1],
            [0, 0, 1, 0, 1, 1, 1],
            [0, 1, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 1]]

    n = len(maze)
    path = [[0 for i in range(n)] for i in range(n)]
    print_maze(maze, n)

    r = 0
    c = 0

    path[r][c] = 1

    move_row = [0, 1,  0, -1]
    move_col = [1, 0, -1,  0]

    visited = ([[r, c]])

    if not proceed_through_maze(maze, path, n, r, c, move_row, move_col, visited):
        print("Solution does not exist")
    else:
        print_maze(path, n)


def test_is_in_maze():
    """
        test is in maze function
    """

    n = 4
    path = [[0 for i in range(n)] for i in range(n)]
    counter = 0
    for i in range(n):
        for j in range(n):
            path[i][j] = counter
            counter += 1
    print(path)

    for i in range(n):
        for j in range(n):
            print(i, j, path[i][j])
            print(is_in_maze(i, j, n))


# Driver program to test above function
if __name__ == "__main__":
    traverse_maze()
