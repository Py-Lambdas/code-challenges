import unittest

from line import Line


class LineTests(unittest.TestCase):
    def test_init(self):
        line = Line((3, 10), (6, -4))
        self.assertTrue(hasattr(line, "point_a"))
        self.assertTrue(hasattr(line, "point_b"))
        self.assertEqual(line.point_a, (3, 10))
        self.assertEqual(line.point_b, (6, -4))

    def test_str(self):
        line = Line((3, 10), (6, -4))
        self.assertFalse(str(line).startswith("<line.Line"))

    def test_translate(self):
        line = Line((3, 10), (6, -4))
        line.translate_x(4)
        self.assertEqual(line.point_a, (7, 10))
        self.assertEqual(line.point_b, (10, -4))
        line.translate_y(-10)
        self.assertEqual(line.point_a, (7, 0))
        self.assertEqual(line.point_b, (10, -14))

    def test_equality(self):
        line1 = Line((1, 2), (3, 4))
        line2 = Line((2, 3), (4, 5))
        line3 = Line((3, 4), (1, 2))
        line4 = Line((1, 4), (1, 2))
        line5 = Line((0, 0), (0, 0))
        line6 = Line((0, 0), (0, 0))
        self.assertTrue(line1 == line2)
        self.assertTrue(line2 == line3)
        self.assertFalse(line3 == line4)
        self.assertTrue(line5 == line6)
        self.assertFalse(line5 == 7)

    def test_comparison(self):
        line1 = Line((0, 0), (2, 2))
        line2 = Line((3, 2), (-2, -2))
        self.assertGreater(line2, line1)
        self.assertFalse(line1 > 7)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_distance(self):
        line = Line((10, 6), (6, -1))
        self.assertEqual(line.distance, 8.06225774829855)
        line.point_a = (9, 6)
        self.assertEqual(line.distance, 7.615773105863909)


if __name__ == "__main__":
    unittest.main(verbosity=2)
