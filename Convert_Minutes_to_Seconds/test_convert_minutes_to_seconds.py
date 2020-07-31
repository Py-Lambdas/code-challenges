import unittest
from convert_minutes_to_seconds import *


class ConvertMinutesToSeconds(unittest.TestCase):
    def test(self):
        self.assertEqual(convert(6), 360)
        self.assertEqual(convert(4), 240)
        self.assertEqual(convert(8), 480)
        self.assertEqual(convert(60), 3600)


if __name__ == "__main__":
    unittest.main()
