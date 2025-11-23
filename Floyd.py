import pandas as pd

edges_data = [
    (1, 7, 1), (1, 4, 1), (1, 2, 2), (1, 3, 5),
    (7, 8, 6), (7, 4, 9), (7, 3, 4),
    (8, 6, 1),
    (6, 3, 4), (6, 4, 5), (6, 5, 3),
    (5, 3, 2), (5, 4, 9), (5, 2, 7),
    (2, 4, 3)
]
num_vertices = 8
INF = float('inf')

W = [[INF] * num_vertices for _ in range(num_vertices)]

for i in range(num_vertices):
    W[i][i] = 0

for u, v, w in edges_data:
    W[u - 1][v - 1] = w
    W[v - 1][u - 1] = w


def floyd(W):
    n = len(W)
    D = [row[:] for row in W]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D


def print_matrix(matrix, title):
    print(f"\n--- {title} ---")
    formatted_matrix = [
        [('∞' if x == INF else x) for x in row]
        for row in matrix
    ]
    df = pd.DataFrame(formatted_matrix,
                      index=range(1, num_vertices + 1),
                      columns=range(1, num_vertices + 1))
    print(df)


print_matrix(W, "Початкова матриця ваг (W)")
shortest_paths = floyd(W)
print_matrix(shortest_paths, "Матриця найкоротших шляхів (D)")