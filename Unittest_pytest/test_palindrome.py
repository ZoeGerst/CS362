import unittest
import pytest
import palindrome


class test_palindrome(unittest.TestCase):

    def test_isPal(self):

        self.assertEqual(palindrome.isPalindrome("madam"), "It is a palindrome.")

    def test_isNotPal(self):

        self.assertEqual(palindrome.isPalindrome("hello"), "It is not a palindrome.")

if __name__ == '__main__':

    unittest.main()
