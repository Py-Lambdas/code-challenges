import unittest

from secrets import secrets


class SecretsTest(unittest.TestCase):
    def test_secrets(self):
        res = secrets('ifmmpXPSME', -1)
        self.assertEqual(res, 'hello world')
        res = secrets('mxxKAGDnmeqMDQnqxazsFAge', 40)
        self.assertEqual(res, 'all your base are belong to us')
        res = secrets('XPSMEifmmp', -1)
        self.assertEqual(res, 'world hello')


if __name__ == "__main__":
    unittest.main(verbosity=2)
