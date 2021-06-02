import unittest
import fizzbuzz

class TestCase(unittest.TestCase):

    def test_3(self):

        self.assertEqual(fizzbuzz.fib(6), "Fizz")

    def test_5(self):

        self.assertEqual(fizzbuzz.fib(40), "Buzz")


if __name__ == '__main__':
    unittest.main()