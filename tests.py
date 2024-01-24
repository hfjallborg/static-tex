import unittest

from static_tex import _check_valid_slug


class TestServerFunctions(unittest.TestCase):

    def test_check_slug(self):
        self.assertTrue(_check_valid_slug('foobar'))
        self.assertTrue(_check_valid_slug('bar-foo'))

        self.assertFalse(_check_valid_slug('Foobar'))
        self.assertFalse(_check_valid_slug('foo_bar'))
        self.assertFalse(_check_valid_slug('bar/foo'))


if __name__ == '__main__':
    unittest.main()
