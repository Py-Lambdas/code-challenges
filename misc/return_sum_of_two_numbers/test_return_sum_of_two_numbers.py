import unittest
from return_sum_of_two_numbers import *


class ReturnSumTwoNumbersTests(unittest.TestCase):
    def test(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-3, -6), -9)
        self.assertEqual(addition(7, 3), 10)


if __name__ == "__main__":
    unittest.main()
