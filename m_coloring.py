# m Coloring - Backtracking


def m_coloring(g, c):
    """
        set initial values for recursive solver
    """

    i = 0
    sol = [0 for _ in range(len(g))]
    sol[i] = c[0]
    if m_coloring_solver(g, c, i + 1, sol):
        return sol
    else:
        print('No solution exists')
        return None


def m_coloring_solver(g, colors, i, sol):

    if not any(x == 0 for x in sol):
        return True

    row = g[i]

    v = []
    for j, col in enumerate(row):
        if col == 0 or i == j:
            continue
        v.append(sol[j])
    for c in colors:
        if c not in v:
            sol[i] = c
            if m_coloring_solver(g, colors, i + 1, sol):
                return True
            print('\nbacktracking\n')
            print_matrix(g, sol)
            sol[i] = 0
    return False


def print_matrix(matrix, sol):
    for i, row in enumerate(matrix):
        matrix[i][i] = sol[i]
        print(matrix[i])


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

    c_ = ['R', 'G', 'B']

    test_graph = g2

    sol = m_coloring(test_graph, c_)
    print('\n', sol, '\n')

    if sol is not None:
        print_matrix(test_graph, sol)