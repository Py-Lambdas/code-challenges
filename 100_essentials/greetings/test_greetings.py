from inspect import getfullargspec, signature
import unittest

from greetings import greetings


class GreetingsTest(unittest.TestCase):
    def test_required_args(self):
        argsspec = getfullargspec(greetings)
        self.assertEqual(len(argsspec.args), 1)
        self.assertIsNotNone(argsspec.kwonlyargs)
        self.assertEqual(greetings('Dave', punctuation='!'), 'Hello, Dave!')

    def test_default_kw(self):
        argsspec = getfullargspec(greetings)
        self.assertIsNotNone(argsspec.kwonlydefaults)
        self.assertEqual(len(argsspec.kwonlydefaults), 1)
        self.assertIn('msg', argsspec.kwonlydefaults)
        self.assertEqual(argsspec.kwonlydefaults['msg'], 'Hello')
        self.assertEqual(greetings('Mark', msg='Oh, hi',
                                   punctuation='.'), 'Oh, hi, Mark.')

    def test_stargs(self):
        argsspec = getfullargspec(greetings)
        self.assertIsNotNone(argsspec.varargs)
        res = greetings('Bob', 'builder', 'tinker', 'tailor',
                        'soldier', 'spy', msg='Hi', punctuation='.')
        test = 'Hi, Bob, the builder, the tinker, the tailor, the soldier, the spy.'
        self.assertEqual(res, test)

    def test_kwargs(self):
        argsspec = getfullargspec(greetings)
        self.assertIsNotNone(argsspec.varkw)
        res = greetings('Dave', msg='Hi', punctuation='!',
                        Mark='Howdy', Jim='You owe me money')
        test = 'Hi, Dave! Mark says "Howdy". Jim says "You owe me money".'
        self.assertEqual(res, test)

    def test_annotations(self):
        self.assertIsNotNone(greetings.__doc__,
                             msg="Add a doc string to greetings function.")
        sig = signature(greetings)
        for p in sig.parameters:
            self.assertNotEqual(
                sig.parameters[p].annotation, sig.parameters[p].empty)
        print(sig.return_annotation)
        self.assertNotEqual(
            sig.return_annotation,
            sig.parameters[p].empty,
            msg="greetings function should have a return annotation",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
