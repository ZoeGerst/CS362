import unittest
import fizzbuzz

class TestCase(unittest.TestCase):

    def test3(self):

        self.assertEqual(fizzbuzz.fib(6), "Fizz")


if __name__ == '__main__':
    unittest.main()