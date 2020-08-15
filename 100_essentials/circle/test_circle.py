import math
import unittest

from circle import Circle


class CircleTests(unittest.TestCase):
    def test_radius(self):
        """
        A circle should take a radius as an argument, and that radius
        sholud be accessible as an attribute.
        """
        circle = Circle(5)
        self.assertEqual(circle.radius, 5)

    def test_default_radius(self):
        """
        If no radius is provided, the radius should default to `1`.
        """
        circle = Circle()
        self.assertEqual(circle.radius, 1)

    def test_diameter(self):
        """
        The diameter of a circle should always be the radius of the circle times 2.
        """
        circle = Circle(2)
        self.assertEqual(circle.diameter, 4)

    def test_area(self):
        """
        The area of a circle should always be `π * diameter`
        """
        circle = Circle(2)
        self.assertEqual(circle.area, math.pi * 4)
        circle = Circle(1)
        self.assertEqual(circle.area, math.pi)

    def test_string_representation(self):
        """
        Circle should have a both a `str` representation and a `repr`
        representation equal to `Circle(radius)`
        """
        circle = Circle(2)
        self.assertEqual(str(circle), "Circle(2)")
        self.assertEqual(repr(circle), "Circle(2)")
        circle.radius = 1
        self.assertEqual(repr(circle), "Circle(1)")

    def test_diameter_and_area_change_based_on_radius(self):
        """
        Both the area and the diameter of the circle should update
        automatically when the radius changes.
        """
        circle = Circle(2)
        self.assertEqual(circle.diameter, 4)
        circle.radius = 3
        self.assertEqual(circle.diameter, 6)
        self.assertEqual(circle.area, math.pi * 9)

    def test_diameter_changeable_but_area_not(self):
        """
        The value of diameter should *also* be changable, and should update
        the radius automatically, but the area should raise an error when a
        caller attempts to change the value
        """
        circle = Circle(2)
        self.assertEqual(circle.diameter, 4)
        self.assertEqual(circle.area, math.pi * 4)
        circle.diameter = 3
        self.assertEqual(circle.radius, 1.5)
        with self.assertRaises(AttributeError):
            circle.area = 3

    def test_no_negative_radius(self):
        """
        A `ValueError` exception with the message 'radius cannot be negative'
        should be raised if a negative number is supplied for the radius.
        """
        with self.assertRaises(ValueError) as context:
            circle = Circle(-2)
        self.assertEqual(
            str(context.exception).lower(), "radius cannot be negative",
        )
        circle = Circle(2)
        with self.assertRaises(ValueError) as context:
            circle.radius = -10
        self.assertEqual(
            str(context.exception).lower(), "radius cannot be negative",
        )
        with self.assertRaises(ValueError):
            circle.diameter = -20
        self.assertEqual(circle.radius, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
