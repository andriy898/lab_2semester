from collections import deque

def read_input(filename):
    with open(filename, 'r') as f:
        start = tuple(map(int, f.readline().strip().split(',')))
        end = tuple(map(int, f.readline().strip().split(',')))
        rows, cols = map(int, f.readline().strip().split(','))
        matrix = []
        for _ in range(rows):
            row = list(map(int, f.readline().strip().strip('[]').split()))
            matrix.append(row)
    return start, end, rows, cols, matrix

def is_valid(x, y, rows, cols, matrix, visited):
    return 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 1 and not visited[x][y]

def bfs(start, end, rows, cols, matrix):
    queue = deque()
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == end:
            return dist
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, rows, cols, matrix, visited):
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, dist + 1))
    
    return -1
    
def main():
    start, end, rows, cols, matrix = read_input('input.txt')
    shortest_path = bfs(start, end, rows, cols, matrix)
    with open('output.txt', 'w') as f:
        f.write(str(shortest_path))

if __name__ == "__main__":
    main()