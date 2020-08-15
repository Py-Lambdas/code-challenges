import unittest


from tail import tail


class TailTests(unittest.TestCase):
    def test_zero(self):
        """
        Return an empty list when `n` is 0
        """
        self.assertEqual(tail([1, 2], 0), [])

    def test_one(self):
        """
        Return the last item in the iterable when `n` is 1
        """
        self.assertEqual(tail([1, 2], 1), [2])

    def test_two(self):
        """
        Return the last two items in the iterable when `n` is 2
        """
        self.assertEqual(tail([1, 2], 2), [1, 2])

    def test_n_larger_than_iterable_length(self):
        """
        Return an empty list when `n` is greater than the number of items in
        the iterable
        """
        nums = [1, 2, 3, 4]
        self.assertEqual(tail(nums, 5), [1, 2, 3, 4])
        self.assertEqual(tail([], 10), [])

    def test_string(self):
        """
        Return a list containing the last `n` characters when the iterable
        is a string
        """
        self.assertEqual(tail("hello", 2), ["l", "o"])

    def test_tuple(self):
        """
        Return a list containing the last `n` items when the iterable is a
        tuple
        """
        self.assertEqual(tail((1, 2, 3), 3), [1, 2, 3])

    def test_negative_n(self):
        """
        Return an empty list when `n` is negative
        """
        nums = [1, 2, 3, 4]
        self.assertEqual(tail(nums, -1), [])
        self.assertEqual(tail((), -9), [])

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_iterator(self):
        """
        Return a list containing the last `n` items in an iterable of any kind,
        not just a sequence type (i.e. a generator and not just a string)
        """
        nums = (n ** 2 for n in [1, 2, 3, 4])
        self.assertEqual(tail(nums, -1), [])  # Don't loop for negative n
        self.assertEqual(tail(nums, 0), [])  # Don't loop for n=0
        self.assertEqual(tail(nums, 2), [9, 16])  # Consuming the generator
        self.assertEqual(list(nums), [])  # The nums generator is now empty
        self.assertEqual(tail(nums, 1), [])  # n=1 with a now empty generator


if __name__ == "__main__":
    unittest.main(verbosity=2)
