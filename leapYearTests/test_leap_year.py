import unittest
import pytest
import leap_year

class TestCase(unittest.TestCase):
	def test_is(self):
		self.assertEqual(leap_year.check(2020), "{0} is a leap year");

	def test_is_not(self):
		self.assertEqual(leap_year.check(2021), "{0} is not a leap year");

if __name__ == '__main__':
	unittest.main();