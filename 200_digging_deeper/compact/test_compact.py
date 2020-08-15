import unittest


from compact import compact


class CompactTests(unittest.TestCase):
    def assertIterableEqual(self, iterable1, iterable2):
        self.assertEqual(list(iterable1), list(iterable2))

    def test_no_duplicates(self):
        self.assertIterableEqual(compact([1, 2, 3]), [1, 2, 3])

    def test_adjacent_duplicates(self):
        self.assertIterableEqual(compact([1, 1, 2, 2, 3]), [1, 2, 3])

    def test_non_adjacent_duplicates(self):
        self.assertIterableEqual(compact([1, 2, 3, 1, 2]), [1, 2, 3, 1, 2])

    def test_lots_of_adjacent_duplicates(self):
        self.assertIterableEqual(compact([1, 1, 1, 1, 1, 1]), [1])

    def test_empty_values(self):
        self.assertIterableEqual(compact([None, 0, "", []]), [None, 0, "", []])

    def test_empty_list(self):
        self.assertIterableEqual(compact([]), [])

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_accepts_iterator(self):
        nums = (n ** 2 for n in [1, 2, 3])
        self.assertIterableEqual(compact(nums), [1, 4, 9])

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_returns_iterator(self):
        nums = (n ** 2 for n in [1, 2, 3])
        output = compact(nums)

        self.assertEqual(iter(output), iter(output))
        self.assertEqual(next(output), 1)

        # The below line tests that the incoming iterator isn't exhausted.
        # It may look odd to test the squares input, but this is correct
        # because after 1 item has been consumed from the compact
        # iterator, nums should only have 1 item consumed as well
        self.assertEqual(next(nums), 4)

        # A more extreme example: calling compact with an infinite iterator
        from itertools import count

        tens = compact(round(n, -1) for n in count())
        self.assertEqual([next(tens) for _ in range(3)], [0, 10, 20])


if __name__ == "__main__":
    unittest.main()
