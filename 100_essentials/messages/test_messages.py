import unittest

from messages import fix_message


class MessagesTests(unittest.TestCase):
    def test_capatalize(self):
        self.assertEqual(fix_message('a message'), 'A message')

    def test_replace(self):
        self.assertEqual(fix_message('xoxo'), '')
        self.assertEqual(fix_message('xoxo something xoxo'), ' something ')
        self.assertEqual(fix_message('xoxostuff'), 'Stuff',
                         msg="Remove xoxo first and then capitalize.")

    def test_empty(self):
        self.assertIsNone(fix_message(''))

    def test_over_50(self):
        msg = "we interrupt this program to annoy you and make things generally more irritating."
        res = 'We interrupt this program to annoy you and make th'
        self.assertEqual(fix_message(msg), res)


if __name__ == "__main__":
    unittest.main(verbosity=2)
