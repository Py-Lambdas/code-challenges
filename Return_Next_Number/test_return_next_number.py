import unittest
from return_next_number import *


class ReturnNextNumber(unittest.TestCase):
    def test(self):
        self.assertEqual(addition(2), 3, "2 plus 1 equals 3.")
        self.assertEqual(addition(-9), -8, "-9 plus 1 equals -8.")
        self.assertEqual(addition(999), 1000, "999 plus 1 equals 1000.")
        self.assertEqual(addition(73), 74, "73 plus 1 equals 74.")

if __name__ == '__main__': 
    unittest.main() 
