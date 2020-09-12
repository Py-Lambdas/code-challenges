import unittest

from log_transfer import log_transfer


class LogTransferTests(unittest.TestCase):
    def test_int(self):
        self.assertEqual(log_transfer(53), "Deposited $53")
        self.assertEqual(log_transfer(-8), "Withdrew $8")
        self.assertEqual(log_transfer(0), "Balance unchanged")

    def test_float(self):
        self.assertEqual(log_transfer(-243.1263), "Withdrew $243.13")
        self.assertEqual(log_transfer(3654.0), "Deposited $3654.00")
        self.assertEqual(log_transfer(0.006), "Deposited $0.01")
        self.assertEqual(log_transfer(0.0), "Balance unchanged")
        self.assertEqual(log_transfer(-0.002), "Balance unchanged")

    def test_string(self):
        self.assertEqual(log_transfer("40.066"), "Deposited $40.07")
        self.assertEqual(log_transfer("-34"), "Withdrew $34.00")
        self.assertEqual(log_transfer("0"), "Balance unchanged")

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_exceptions(self):
        with self.assertRaises(TypeError) as context:
            log_transfer(True)
        self.assertEqual(
            str(context.exception).lower(),
            "x must be a string, int, or float",
        )
        with self.assertRaises(ValueError) as context:
            log_transfer("ALLTHEMONIES")
        self.assertEqual(
            str(context.exception).lower(),
            "x is not a valid number",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
