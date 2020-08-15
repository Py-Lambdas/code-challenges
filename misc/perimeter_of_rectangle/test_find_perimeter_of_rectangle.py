import unittest
from find_perimeter_of_rectangle import *


class PerimeterOfRectangle(unittest.TestCase):
    def test_find_perimeter(self):
        self.assertEqual(find_perimeter(6, 7), 26)
        self.assertEqual(find_perimeter(20, 10), 60)
        self.assertEqual(find_perimeter(2, 9), 22)


if __name__ == "__main__":
    unittest.main()
