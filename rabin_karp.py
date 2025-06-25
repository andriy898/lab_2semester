import unittest







from main import rabin_karp




class TestRabinKarp(unittest.TestCase):


   def test_rabin_karp_empty_haystack(self):
       result = rabin_karp("", "needle")
       self.assertEqual(result, [])


   def test_rabin_karp_empty_needle(self):
       result = rabin_karp("haystack", "")
       self.assertEqual(result, [])


   def test_rabin_karp_exact_match(self):
       result = rabin_karp("hello world", "world")
       self.assertEqual(result, [6])


   def test_rabin_karp_multiple_matches(self):
       result = rabin_karp("ababab", "ab")
       self.assertEqual(result, [0, 2, 4])


   def test_rabin_karp_no_match(self):
       result = rabin_karp("abcdefg", "xyz")
       self.assertEqual(result, [])


   def test_rabin_karp_case_sensitive(self):
       result = rabin_karp("Hello World", "hello")
       self.assertEqual(result, [])


   def test_rabin_karp_single_char_needle(self):
       result = rabin_karp("abcdefg", "c")
       self.assertEqual(result, [2])


   def test_rabin_karp_large_input(self):
       haystack = "a" * 10 ** 6
       needle = "a" * 1000
       result = rabin_karp(haystack, needle)
       self.assertEqual(result, [i for i in range(10 ** 6 - 999)])




if __name__ == '__main__':
   unittest.main()
