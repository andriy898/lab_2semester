import unittest
from lab_1V_2R import marichka_method


test_5x5 = [[1, 2, 3, 4, 5],
           [10, 9, 8, 7, 6],
           [11, 12, 13, 14, 15],
           [20, 19, 18, 17, 16],
           [21, 22, 23, 24, 25]]


test_2x4 = [[1, 2],
           [4, 3],
           [5, 6],
           [8, 7]]


test_6x1 = [[1], [2], [3], [4], [5], [6]]




class Test(unittest.TestCase):
   def test_5x5_marichka(self):
       expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
       self.assertEqual(marichka_method(test_5x5), expected)


   def test_2x4_marichka(self):
       expected = [1, 2, 3, 4, 5, 6, 7, 8]
       self.assertEqual(marichka_method(test_2x4), expected)


   def test_6x1_marichka(self):
       expected = [1, 2, 3, 4, 5, 6]
       self.assertEqual(marichka_method(test_6x1), expected)


   def test_empty(self):
       self.assertEqual(marichka_method([]), [])


   def test_none(self):
       self.assertEqual(marichka_method(None), [])