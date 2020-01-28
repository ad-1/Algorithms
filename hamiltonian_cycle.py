# Hamiltonian Cycle - Backtracking Algorithm

"""
    Hamiltonian Path in an undirected or directed graph is a
    path that visits each vertex exactly once.
"""

from timeit import default_timer as timer


def get_col(board, r, c):
    """
        get column elements for given column number
    """

    col = []
    for row in board:
        col.append(row[c])
    return col


def hamiltonian_cycle(graph):
    """
        main driver method to set initial values for
        recursive solver which will find a hamilton
        path using backtracking algorithm if one exists
    """

    n = len(graph)
    path = [0]
    v = 0
    if solve_hamiltonian_cycle(graph, n, path, v):
        # path = [x + 1 for x in path]
        print(path)
    else:
        print('Hamilton Path is not possible')


def solve_hamiltonian_cycle(graph, n, path, v):
    """
        recursive solver method to find hamiltonian
        cycle if one exists
    """

    if len(path) == n + 1:
        return True

    for c in range(0, n):
        if c == v:
            continue
        if graph[v][c] == 1 and c not in path:
            path.append(c)
            if len(path) == n:
                if graph[path[-1]][path[0]] == 1:
                    path.append(path[0])
                    return True
                path.pop(-1)
                return False
            if solve_hamiltonian_cycle(graph, n, path, c):
                return True
            path.pop(-1)

    return False


# Driver program to test above function
if __name__ == '__main__':

    g1 = [[0, 1, 0, 1, 0],
          [1, 0, 1, 1, 0],
          [0, 1, 0, 1, 1],
          [1, 1, 1, 0, 1],
          [0, 0, 1, 1, 0]]

    g2 = [[0, 1, 0, 1, 0],
          [1, 0, 1, 1, 1],
          [0, 1, 0, 0, 1],
          [1, 1, 0, 0, 1],
          [0, 1, 1, 1, 0]]

    g3 = [[0, 1, 0, 1, 0],
          [1, 0, 1, 1, 1],
          [0, 1, 0, 0, 1],
          [1, 1, 0, 0, 0],
          [0, 1, 1, 0, 0]]

    g4 = [[0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
          [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
          [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
          [0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
          [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
          [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
          [0, 1, 0, 0, 1, 0, 1, 0, 0, 0]]

    g5 = [[0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
          [1, 0, 0, 1, 1, 0, 0, 1, 0, 0],
          [0, 1, 1, 0, 1, 0, 0, 0, 1, 0],
          [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
          [0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
          [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
          [0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
          [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]]

    start = timer()
    hamiltonian_cycle(g5)
    end = timer()
    print('\ncompleted in {} seconds'.format(end - start))
