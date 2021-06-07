import unittest
import pytest
import reverse

class test_sentence(unittest.TestCase):

    def test_input(self):

        self.assertEqual(reverse("My name is Zoe"), "Zoe is name My")

if __name__ == '__main__':

    unittest.main()