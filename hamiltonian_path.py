# Hamiltonian Cycle - Backtracking Algorithm

"""
Hamiltonian Path in an undirected or directed graph is a
path that visits each vertex exactly once.
"""


def print_graph(graph):
    """
        print graph matrix
    """

    print()
    for i in range(len(graph)):
        for j in range(len(graph)):
            print(graph[i][j], end=' ')
        print()
    print()


def is_on_graph(graph, v):
    """
        check x,y coordinates are in the maze
    """

    if 0 <= v[0] < len(graph) and 0 <= v[1] < len(graph):
        return True
    return False


def hamiltonian_path(graph):
    """
        main driver method to set initial values for
        recursive solver which will find a hamilton
        path using backtracking algorithm if one exists
    """

    n = len(graph)
    cycle = []
    print_graph(graph)
    if solve_hamiltonian_path(graph, n, cycle):
        print(cycle)
    else:
        print('Hamilton Path is not possible')


def solve_hamiltonian_path(graph, n, cycle):

    if len(cycle) == n:
        return True

    for i in range(len(graph)):

        print(graph[i][i])


# Driver program to test above function
if __name__ == '__main__':
    g = [[0, 1, 0, 1, 0],  # 0 [0, 0]
         [1, 0, 1, 1, 0],  # 1 [1, 1]
         [0, 1, 0, 1, 1],  # 2 [2, 2]
         [1, 1, 1, 0, 1],  # 3 [3, 3]
         [0, 0, 1, 1, 0]]  # 4 [4, 4]

    hamiltonian_path(g)
