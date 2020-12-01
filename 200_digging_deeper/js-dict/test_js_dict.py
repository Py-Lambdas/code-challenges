import unittest


from js_dict import JSDict


class JSDictTests(unittest.TestCase):

    """Tests for JSDict."""

    def test_constructor(self):
        JSDict()
        JSDict({"a": 2, "b": 3})

    def test_key_access(self):
        d = JSDict({"a": 2, "b": 3})
        self.assertEqual(d["a"], 2)
        self.assertEqual(d["b"], 3)

    def test_attribute_access(self):
        d = JSDict({"a": 2, "b": 3})
        self.assertEqual(d.a, 2)
        self.assertEqual(d.b, 3)

    def test_original_dictionary_unchanged(self):
        mapping = {"a": 2, "b": 3}
        d = JSDict(mapping)
        d.c = 4
        self.assertEqual(mapping, {"a": 2, "b": 3})

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_allow_setting_keys_and_attributes(self):
        d = JSDict({"a": 2, "b": 3})
        d["a"] = 4
        self.assertEqual(d["a"], 4)
        self.assertEqual(d.a, 4)
        d.c = 9
        self.assertEqual(d["c"], 9)
        self.assertEqual(d.c, 9)
        self.assertEqual(d["b"], 3)
        x = JSDict()
        y = JSDict()
        x.a = 4
        y.a = 5
        self.assertEqual(x.a, 4)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_keyword_arguments_equality_and_get_method(self):
        d = JSDict(a=2, b=3, c=4, d=5)
        self.assertEqual(d.a, 2)
        self.assertEqual(d.b, 3)
        self.assertEqual(d["c"], 4)
        self.assertEqual(d["d"], 5)
        x = JSDict({"a": 2, "b": 3})
        y = JSDict({"a": 2, "b": 4})
        self.assertNotEqual(x, y)
        y.b = 3
        self.assertEqual(x, y)
        x.c = 5
        self.assertNotEqual(x, y)
        y.c = 5
        self.assertEqual(x, y)
        self.assertIsNone(y.get("d"))
        self.assertEqual(y.get("c"), 5)
        self.assertEqual(y.get("d", 5), 5)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_normalize_arg(self):
        d = JSDict({"greeting 1": "hi"}, normalize=True)
        self.assertEqual(d["greeting 1"], "hi")
        self.assertEqual(d.greeting_1, "hi")
        d.greeting_2 = "hello"
        self.assertEqual(d["greeting 2"], "hello")
        self.assertEqual(d.greeting_2, "hello")
        d["greeting 2"] = "hey"
        self.assertEqual(d["greeting 2"], "hey")
        self.assertEqual(d.get("greeting 2"), "hey")
        self.assertEqual(d.greeting_2, "hey")
        with self.assertRaises(AttributeError):
            d.greeting2
        d = JSDict({"greeting 1": "hi"})
        self.assertEqual(d["greeting 1"], "hi")
        with self.assertRaises(AttributeError):
            d.greeting_1


if __name__ == "__main__":
    unittest.main(verbosity=2)
