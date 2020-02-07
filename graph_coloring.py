# Graph Coloring (m Coloring Problem) - Backtracking Algorithm

"""
    'm Coloring Problem'
    Given an undirected graph and a number m, determine if the graph
    can be colored with at most m colors such that no two adjacent
    vertices of the graph are colored with same color.
    Coloring of a graph means assignment of colors to all vertices.
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
        check vertex coordinates are in the graph
    """

    if 0 <= v[0] < len(graph) and 0 <= v[1] < len(graph):
        return True
    return False


def get_vertices(graph):
    """
        return all vertices in the graph
    """

    vertices = []
    for row_index, row in enumerate(graph):
        for col_index, col in enumerate(row):
            if graph[row_index][col_index] != 0:
                vertices.append([row_index, col_index])
    return vertices


def are_connected_diagonally(v1, v2):
    """
        given two coordinates, check if
        they are connected diagonally
    """

    if abs(v1[0]-v2[0]) == abs(v1[1] - v2[1]):
        return True
    return False


def check_upper_vertices(graph, v, c):
    """
        check if either upper vertex is already
        assigned to a given color
    """

    ulv = [v[0] - 1, v[1] - 1]
    urv = [v[0] - 1, v[1] + 1]
    uvs = [ulv, urv]
    for uv in uvs:
        if not is_on_graph(graph, uv):
            continue
        if graph[uv[0]][uv[1]] == c:
            return False
    return True


def check_hv_nodes(graph, v, c):
    """
        check if the preceding horizontal or vertical
        node has the color
    """

    if graph[v[0]][v[1]-1] == c or graph[v[0]-1][v[1]] == c:
        return False
    return True


def can_assign_color(graph, v, c):
    """
        validate that a color can be entered in given vertex
    """

    if is_on_graph(graph, v) \
            and check_upper_vertices(graph, v, c) \
            and check_hv_nodes(graph, v, c):
        return True
    return False


def m_coloring(graph, colors):
    """
        driver method to set initial values
        for the m coloring problem
    """

    print_graph(graph)
    vertices = get_vertices(graph)
    if solve_m_coloring(graph, colors, vertices, 0):
        print_graph(graph)
    else:
        print('No solution exists')


def solve_m_coloring(graph, colors, vertices, pos):
    """
        recursive method to solve m coloring
        problem using backtracking
    """

    if pos == len(vertices):
        return True

    v = vertices[pos]

    for c in colors:
        if can_assign_color(graph, v, c):
            graph[v[0]][v[1]] = c
            pos += 1
            if solve_m_coloring(graph, colors, vertices, pos):
                return True
            pos -= 1
            graph[v[0]][v[1]] = 1

    return False


# Driver program to test above function
if __name__ == '__main__':
    g = [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 1, 0]]

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

    c_ = ['r', 'g', 'b']
    m_coloring(g5, c_)
