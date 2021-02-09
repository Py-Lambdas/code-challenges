import unittest

from format_ranges import format_ranges


class FormatRangesTests(unittest.TestCase):

    """Tests for format_ranges."""

    def test_one_group(self):
        self.assertEqual(format_ranges([1, 2, 3]), '1-3')

    def test_two_groups(self):
        self.assertEqual(
            format_ranges([1, 2, 10, 11, 12, 13, 14]),
            '1-2,10-14'
        )

    def test_three_groups(self):
        self.assertEqual(
            format_ranges([4, 5, 16, 17, 18, 20, 21]),
            '4-5,16-18,20-21'
        )

    def test_non_sequences(self):
        self.assertEqual(
            format_ranges(iter([4, 5, 16, 17, 18, 20, 21])),
            '4-5,16-18,20-21'
        )

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_lone_numbers(self):
        self.assertEqual(format_ranges([1]), '1')
        self.assertEqual(format_ranges([4, 16, 18]), '4,16,18')
        self.assertEqual(format_ranges([1, 10, 11, 12, 13, 14]), '1,10-14')

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_unordered_numbers(self):
        self.assertEqual(format_ranges([10, 20, 12, 3, 11]), '3,10-12,20')

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_duplicate_numbers(self):
        self.assertEqual(
            format_ranges([10, 20, 10, 12, 11, 20]),
            '10,10-12,20,20'
        )
        self.assertEqual(
            format_ranges([10, 11, 20, 10, 12, 11, 12]),
            '10-12,10-12,20'
        )
        self.assertEqual(
            format_ranges([1, 9, 1, 7, 3, 8, 2, 4, 2, 4, 7]),
            '1-2,1-4,4,7,7-9'
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)