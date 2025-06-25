import pandas as pd
import numpy as np

def minimum_cable_length(filename):

    df = pd.read_csv(filename, header=None)
    matrix = df.values
    N = len(matrix)

    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            if matrix[i][j] > 0:
                edges.append((matrix[i][j], i, j))

    edges.sort()
    parent = list(range(N))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX
            return True
        return False

    total_length = 0
    for weight, u, v in edges:
        if union(u, v):
            total_length += weight

    return total_length
