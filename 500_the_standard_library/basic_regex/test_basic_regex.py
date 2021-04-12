import unittest

from basic_regex import is_valid_send_off


class RegexTest(unittest.TestCase):
    def test_name(self):
        sentence = "Hey Bob, email@email.com, yep."
        name = "Bob"
        res = is_valid_send_off(sentence, name)
        self.assertTrue(res)

        sentence = "Hey Rachel, email@email.com, yep."
        name = "Bob"
        res = is_valid_send_off(sentence, name)
        self.assertFalse(res)

    def test_grammar(self):
        sentence = "Hey Bob, email@email.com, yep."
        name = "Bob"
        res = is_valid_send_off(sentence, name)
        self.assertTrue(res)

        sentence = "Hey Bob, email@email.com, yep?"
        res = is_valid_send_off(sentence, name)
        self.assertTrue(res)

        sentence = "Hey Bob, email@email.com, yep!"
        res = is_valid_send_off(sentence, name)
        self.assertTrue(res)

        sentence = "hey Bob, email@email.com, yep."
        res = is_valid_send_off(sentence, name)
        self.assertFalse(res)

        sentence = "? Hey Bob, email@email.com, yep."
        res = is_valid_send_off(sentence, name)
        self.assertFalse(res)

        sentence = "Hey Bob, email@email.com, yep"
        res = is_valid_send_off(sentence, name)
        self.assertFalse(res)

    def test_email(self):
        sentence = "Hey Bob, email@email.com, yep."
        name = "Bob"
        res = is_valid_send_off(sentence, name)
        self.assertTrue(res)

        sentence = "Hey Bob, email.com, yep."
        res = is_valid_send_off(sentence, name)
        self.assertFalse(res)

        sentence = "Hey Bob, email@.com, yep."
        res = is_valid_send_off(sentence, name)
        self.assertFalse(res)

        sentence = "Hey Bob, email@email. , yep."
        res = is_valid_send_off(sentence, name)
        self.assertFalse(res)

    # def bonus(self):
    #     sentence = "Hey Bob, email@email@email.com, yep."
    #     name = "Bob"
    #     res = is_valid_send_off(sentence, name)
    #     self.assertFalse(res)

    #     sentence = "Hey Bob, first.last@student.email.com, yep."
    #     res = is_valid_send_off(sentence, name)
    #     self.assertTrue(res)


if __name__ == "__main__":
    unittest.main(verbosity=2)
