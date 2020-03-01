# Grid Adjacency Matrix - Graph Theory


def adjacency_matrix(rows, cols):
    n = rows * cols
    m = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(rows):
        for c in range(cols):
            i = r * cols + c
            if c > 0:
                m[i - 1][i] = m[i][i - 1] = 1
            if r > 0:
                m[i - cols][i] = m[i][i - cols] = 1
    return m
