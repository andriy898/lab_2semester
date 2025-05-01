import unittest
from list_based_priority_queue import Priority

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Priority()

    def test_insert_and_peek(self):
        self.queue.insert("Task1", 2)
        self.queue.insert("Task2", 5)
        self.queue.insert("Task3", 1)
        self.assertEqual(self.queue.peek(), "Task2")

    def test_pop(self):
        self.queue.insert("A", 3)
        self.queue.insert("B", 4)
        self.queue.insert("C", 2)
        self.assertEqual(self.queue.pop(), "B")
        self.assertEqual(self.queue.pop(), "A")
        self.assertEqual(self.queue.pop(), "C")
        self.assertIsNone(self.queue.pop())

    def test_order_with_same_priority(self):
        self.queue.insert("X", 5)
        self.queue.insert("Y", 5)
        self.queue.insert("Z", 5)
        self.assertEqual(self.queue.pop(), "X")
        self.assertEqual(self.queue.pop(), "Y")
        self.assertEqual(self.queue.pop(), "Z")

    def test_empty_queue(self):
        self.assertIsNone(self.queue.peek())
        self.assertIsNone(self.queue.pop())

if __name__ == '__main__':
    unittest.main()
