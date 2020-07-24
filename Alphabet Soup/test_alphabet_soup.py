import unittest
from alphabet_soup import *


class ReturnSumTwoNumbersTests(unittest.TestCase):
    def test(self):
        self.assertEqual(alphabet_soup("hello"), "ehllo")
        self.assertEqual(alphabet_soup("edabit"), "abdeit")
        self.assertEqual(alphabet_soup("hacker"), "acehkr")
        self.assertEqual(alphabet_soup("geek"), "eegk")
        self.assertEqual(alphabet_soup("javascript"), "aacijprstv")
        self.assertEqual(alphabet_soup("credibility"), "bcdeiiilrty")
        self.assertEqual(alphabet_soup("apostrophe"), "aehoopprst")
        self.assertEqual(alphabet_soup("determination"), "adeeiimnnortt")
        self.assertEqual(alphabet_soup("win"), "inw")
        self.assertEqual(alphabet_soup("synthesis"), "ehinsssty")


if __name__ == "__main__":
    unittest.main()
