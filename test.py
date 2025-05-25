import unittest
from lab6_1V_2R import topological_sort

class TestTopologicalSort(unittest.TestCase):

    def test_example_case(self):
        dependencies = [
            ("visa", "foreignpassport"),
            ("visa", "hotel"),
            ("visa", "bankstatement"),
            ("bankstatement", "nationalpassport"),
            ("hotel", "creditcard"),
            ("creditcard", "nationalpassport"),
            ("nationalpassport", "birthcertificate"),
            ("foreignpassport", "nationalpassport"),
            ("foreignpassport", "militarycertificate"),
            ("militarycertificate", "nationalpassport"),
        ]

        result = topological_sort(dependencies)

        expected_order = [
            "birthcertificate",
            "nationalpassport",
            "militarycertificate",
            "foreignpassport",
            "creditcard",
            "hotel",
            "bankstatement",
            "visa"
        ]

        index = {doc: i for i, doc in enumerate(result)}
        for later, earlier in dependencies:
            self.assertLess(index[earlier], index[later])

        self.assertEqual(set(result), set(index.keys()))

if __name__ == '__main__':
    unittest.main()
