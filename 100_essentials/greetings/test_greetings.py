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
        self.assertIsNotNone(argspec.defaults,
                             msg="Message should default to 'Hello'")
        self.assertEqual(len(argspec.defaults), 1,
                         msg="Name should be required")
        self.assertEqual(argspec.defaults[0], "Hello")
        self.assertEqual(greet("Greg"), "Hello, Greg!",
                         msg="Greeting should be formatted as message + ', ' + name + '!'")
        self.assertEqual(greet("Greg", "Greetings"), "Greetings, Greg!",
                         msg="Greeting should be formatted as message + ', ' + name + '!'")

    def test_greet_with_style(self):
        argspec = getfullargspec(greet_with_style)
        self.assertEqual(len(argspec.args), 1,
                         msg="greet_withstyle should accept 1 positional argument")
        self.assertNotEqual(
            argspec.varargs, None, msg="greet_with_style should accept an arbitrary amount of positional arguments with *args")
        self.assertEqual(len(argspec.kwonlyargs), 3,
                         msg="greet_with_style should have 3 key word only parameters - msg, sep and punctuation")
        kwonlys = {'msg', 'sep', 'punctuation'}
        self.assertEqual(len(kwonlys - set(argspec.kwonlyargs)), 0)
        self.assertIsNotNone(argspec.kwonlydefaults,
                             msg="Message should default to 'Hello' and the seperator should default to ', '")
        self.assertTrue(
            'msg' in argspec.kwonlydefaults and 'sep' in argspec.kwonlydefaults, msg="Message should default to 'Hello' and the seperator should default to ', '")
        self.assertTrue(argspec.kwonlydefaults['msg'] == 'Hello' and argspec.kwonlydefaults['sep']
                        == ', ', msg="Message should default to 'Hello' and the seperator should default to ', '")
        self.assertEqual(greet_with_style("Mark", msg="Oh, hi",
                                          sep=" ", punctuation="."), "Oh, hi Mark.", msg="greet_with_style should assemble a greeting as msg + sep + name + punctuation")
        self.assertEqual(greet_with_style(
            "Citizen", lambda x: x.upper(), punctuation="!"), "HELLO, CITIZEN!", msg="greet_with_style should return a greeting after applying all functions passed to *args")

        def starify(s):
            return "*".join(list(s))
        self.assertEqual(greet_with_style(
            "Citizen", starify, lambda x: x.upper(), msg="Greetings", punctuation="!", sep="*"), "G*R*E*E*T*I*N*G*S***C*I*T*I*Z*E*N*!", msg="greet_with_style should return a greeting after applying all functions passed to *args")


if __name__ == "__main__":
    unittest.main(verbosity=2)
