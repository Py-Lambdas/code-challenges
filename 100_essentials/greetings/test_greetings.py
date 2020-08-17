from inspect import getfullargspec
import unittest

from greetings import greet, greet_with_style, add_epitaphs


class GreetingsTest(unittest.TestCase):
    def test_greet(self):
        """
        Greet should take 2 parameters, name and msg="Hello"
        Greet should return msg + ", " + name + "!"
        """
        argspec = getfullargspec(greet)
        self.assertEqual(len(argspec.args), 2,
                         msg="Greet should accept 2 arguments")
        self.assertNotEqual(argspec.defaults, None,
                            msg="Message should default to 'Hello'")
        self.assertEqual(len(argspec.defaults), 1,
                         msg="Name should be required")
        self.assertEqual(argspec.defaults[0], "Hello")
        self.assertEqual(greet("Greg"), "Hello, Greg!",
                         msg="Greeting should be formatted as message + ', ' + name + '!'")
        self.assertEqual(greet("Greg", "Greetings"), "Greetings, Greg!",
                         msg="Greeting should be formatted as message + ', ' + name + '!'")


if __name__ == "__main__":
    unittest.main(verbosity=2)
