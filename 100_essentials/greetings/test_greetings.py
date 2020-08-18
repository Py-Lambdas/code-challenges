from inspect import getfullargspec, signature
from typing import Callable
import unittest

from greetings import greet, greet_with_style, add_epitaphs


def cap(x):
    return x.upper()


def starify(s):
    return "*".join(list(s))


class GreetingsTest(unittest.TestCase):
    def test_greet(self):
        """
        Greet should take 2 parameters, name and msg="Hello"
        Greet should return msg + ", " + name + "!"
        """
        argspec = getfullargspec(greet)
        self.assertEqual(len(argspec.args), 2,
                         msg="Greet should accept 2 arguments")
        self.assertIsNotNone(
            argspec.defaults, msg="Message should default to 'Hello'")
        self.assertEqual(len(argspec.defaults), 1,
                         msg="Name should be required")
        self.assertEqual(argspec.defaults[0], "Hello")
        self.assertEqual(
            greet("Greg"),
            "Hello, Greg!",
            msg="Greeting should be formatted as message + ', ' + name + '!'",
        )
        self.assertEqual(
            greet("Greg", "Greetings"),
            "Greetings, Greg!",
            msg="Greeting should be formatted as message + ', ' + name + '!'",
        )

    def test_greet_with_style(self):
        argspec = getfullargspec(greet_with_style)

        self.assertEqual(
            len(argspec.args),
            1,
            msg="greet_withstyle should accept 1 positional argument",
        )
        self.assertNotEqual(
            argspec.varargs,
            None,
            msg="greet_with_style should accept an arbitrary amount of positional arguments with *args",
        )
        self.assertEqual(
            len(argspec.kwonlyargs),
            3,
            msg="greet_with_style should have 3 key word only parameters - msg, sep and punctuation",
        )
        kwonlys = {"msg", "sep", "punctuation"}
        self.assertEqual(len(kwonlys - set(argspec.kwonlyargs)), 0)
        self.assertIsNotNone(
            argspec.kwonlydefaults,
            msg="Message should default to 'Hello' and the seperator should default to ', '",
        )
        self.assertTrue(
            "msg" in argspec.kwonlydefaults and "sep" in argspec.kwonlydefaults,
            msg="Message should default to 'Hello' and the seperator should default to ', '",
        )
        self.assertTrue(
            argspec.kwonlydefaults["msg"] == "Hello"
            and argspec.kwonlydefaults["sep"] == ", ",
            msg="Message should default to 'Hello' and the seperator should default to ', '",
        )
        self.assertEqual(
            greet_with_style("Mark", msg="Oh, hi", sep=" ", punctuation="."),
            "Oh, hi Mark.",
            msg="greet_with_style should assemble a greeting as msg + sep + name + punctuation",
        )
        self.assertEqual(
            greet_with_style("Citizen", cap, punctuation="!"),
            "HELLO, CITIZEN!",
            msg="greet_with_style should return a greeting after applying all functions passed to *args",
        )
        self.assertEqual(
            greet_with_style(
                "Citizen", starify, cap, msg="Greetings", punctuation="!", sep="*",
            ),
            "G*R*E*E*T*I*N*G*S***C*I*T*I*Z*E*N*!",
            msg="greet_with_style should return a greeting after applying all functions passed to *args",
        )

    def test_add_epitaphs(self):
        sig = signature(add_epitaphs)
        params = list(sig.parameters)
        self.assertEqual(
            len(params), 2, msg="add_epitaphs should have 2 parameters")
        name, kwargs = params
        self.assertEqual(
            sig.parameters[name].kind, sig.parameters[name].POSITIONAL_OR_KEYWORD
        )
        self.assertEqual(
            sig.parameters[kwargs].kind, sig.parameters[name].VAR_KEYWORD)
        self.assertEqual(
            add_epitaphs("Gregson", Son="Greg", Leader="Kobolds"),
            "Gregson, Son of Greg, Leader of Kobolds",
            msg="add_epitaphs should add ', {key} of {value}' for all epitaphs in **kwargs to name and return it",
        )
        self.assertEqual(
            greet_with_style(
                add_epitaphs("Gregson", Son="Greg", Leader="Kobolds"),
                cap,
                msg="Hello",
                punctuation="!",
            ),
            "HELLO, GREGSON, SON OF GREG, LEADER OF KOBOLDS!",
        )

    def test_annotations(self):
        self.assertIsNotNone(
            greet_with_style.__doc__, msg="Add a doc string to greet_with_style"
        )
        sig = signature(greet_with_style)
        for p in sig.parameters:
            self.assertNotEqual(
                sig.parameters[p].annotation, sig.parameters[p].empty)

        self.assertEqual(
            sig.return_annotation,
            str,
            msg="greet_with_style should have a return type of str",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
