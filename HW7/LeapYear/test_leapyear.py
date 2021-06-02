import unittest
import leapyear

class TestCase(unittest.TestCase):

    def test_is(self):
        self.assertEqual(leapyear.check(2020), "is a leap year")

    def test_is(self):
        self.assertEqual(leapyear.check(2022), "is not a leap year")


if __name__ == '__main__':
    unittest.main()