import unittest
from lab5_1V_2R import bfs, is_valid

class TestLabyrinth(unittest.TestCase):
    def test_labyrinth_shortest_path(self):
        
        start = (0, 0)
        end = (7, 5)
        rows, cols = 10, 10
        matrix = [
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
        ]

        result = bfs(start, end, rows, cols, matrix)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()
