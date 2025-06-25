import pandas as pd
import numpy as np
import tempfile

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

def test_minimum_cable_length():
    test_matrix = np.array([
        [0, 2, 0, 6],
        [2, 0, 3, 8],
        [0, 3, 0, 0],
        [6, 8, 0, 0]
    ])

    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as tmp:
        pd.DataFrame(test_matrix).to_csv(tmp.name, header=False, index=False)
        filename = tmp.name

    result = minimum_cable_length(filename)
    expected = 11
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✅ Тест пройдено успішно: мінімальна довжина =", result)

test_minimum_cable_length()
