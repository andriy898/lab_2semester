import unittest
from lab2_1V_2R import found_triple_sum


class TestTripleSum(unittest.TestCase):

    def test_case_1(self):
        nums = [1, 2, 3]
        target_sum = 6
        self.assertTrue(found_triple_sum(nums, target_sum))

    def test_case_2(self):
        nums = [1, 4, 0, 6, 10, 1]
        target_sum = 22
        self.assertFalse(found_triple_sum(nums, target_sum))

    def test_case_3(self):
        nums = [1, 2, 3]
        target_sum = 7
        self.assertFalse(found_triple_sum(nums, target_sum))

    def test_case_4(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target_sum = 15
        self.assertTrue(found_triple_sum(nums, target_sum))

    def test_case_lab(self):
        nums = [1, 4, 1000, 20, 700, 300, 8, 6, 500, 501]
        target_sum = 1501
        self.assertTrue(found_triple_sum(nums, target_sum))


if __name__ == '__main__':
    unittest.main()
