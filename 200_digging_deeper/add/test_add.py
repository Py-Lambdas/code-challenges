from copy import deepcopy
import unittest

from add import add


class AddTests(unittest.TestCase):

    """Tests for add."""

    def test_single_items(self):
        self.assertEqual(add([[5]], [[-2]]), [[3]])

    def test_two_by_two_matrixes(self):
        m1 = [[6, 6], [3, 1]]
        m2 = [[1, 2], [3, 4]]
        m3 = [[7, 8], [6, 5]]
        self.assertEqual(add(m1, m2), m3)

    def test_two_by_three_matrixes(self):
        m1 = [[1, 2, 3], [4, 5, 6]]
        m2 = [[-1, -2, -3], [-4, -5, -6]]
        m3 = [[0, 0, 0], [0, 0, 0]]
        self.assertEqual(add(m1, m2), m3)

    def test_input_unchanged(self):
        m1 = [[6, 6], [3, 1]]
        m2 = [[1, 2], [3, 4]]
        m1_original = deepcopy(m1)
        m2_original = deepcopy(m2)
        add(m1, m2)
        self.assertEqual(m1, m1_original)
        self.assertEqual(m2, m2_original)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_any_number_of_matrixes(self):
        m1 = [[6, 6], [3, 1]]
        m2 = [[1, 2], [3, 4]]
        m3 = [[2, 1], [3, 4]]
        m4 = [[9, 9], [9, 9]]
        m5 = [[31, 32], [27, 24]]
        self.assertEqual(add(m1, m2, m3), m4)
        self.assertEqual(add(m2, m3, m1, m1, m2, m4, m1), m5)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_different_matrix_size(self):
        m1 = [[6, 6], [3, 1]]
        m2 = [[1, 2], [3, 4], [5, 6]]
        m3 = [[6, 6], [3, 1, 2]]
        with self.assertRaises(ValueError):
            add(m1, m2)
        with self.assertRaises(ValueError):
            add(m1, m3)
        with self.assertRaises(ValueError):
            add(m1, m1, m1, m3, m1, m1)
        with self.assertRaises(ValueError):
            add(m1, m1, m1, m2, m1, m1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
