import unittest
import pytest
import word_count

class testNumOfWords(unittest.TestCase):

    def test_sentence(self):

        self.assertEqual(word_count("This is an activity"), 4)

if __name__ == '__main__':

    unittest.main()