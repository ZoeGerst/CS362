import unittest
import name_generator

class TestGenerator(unittest.TestCase):

    def test_first_last(self):

        self.assertEqual(name_generator.name("Zoe", "Gerst"), "Zoe Gerts")

    def test_invalid(self):

        self.assertEqual(name_generator.name("123", "456"), "Invalid input.")
    
    def test_blank(self):

        self.assertEqual(name_generator.name("", ""), "No inputs.")

if __name__ == '__main__':

    unittest.main()