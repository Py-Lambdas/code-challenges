import unittest

import coordinates


class coordinatesTests(unittest.TestCase):
    def test_integers(self):
        self.assertIsInstance(coordinates.x1, int)
        self.assertEqual(coordinates.x1, 0)
        self.assertIsInstance(coordinates.y1, int)
        self.assertEqual(coordinates.y1, 4)
        self.assertIsInstance(coordinates.x2, int)
        self.assertEqual(coordinates.x2, 6)
        self.assertIsInstance(coordinates.y2, int)
        self.assertEqual(coordinates.y2, 11)

    def test_slope(self):
        self.assertIsInstance(coordinates.slope, float)
        slope = (11 - 4) / (6 - 0)
        self.assertEqual(coordinates.slope, slope)
        self.assertTrue(slope == coordinates.slope)
        with open("./coordinates.py", "r") as file:
            source_code = file.read()
            self.assertNotIn(
                "1.16",
                source_code,
                msg="No, that's cheating. Code the equation for slope.",
            )

    def test_third_coords(self):
        self.assertIsInstance(coordinates.x3, int)
        self.assertEqual(coordinates.x3, 14)
        self.assertIsInstance(coordinates.y3, int)
        self.assertEqual(coordinates.y3, 20)
        with open("./coordinates.py", "r") as file:
            source_code = file.read()
            self.assertNotIn(
                "20",
                source_code,
                msg="No, that's cheating. Don't hard code the answer. Hint: round(slope * x3 + y1)",
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
