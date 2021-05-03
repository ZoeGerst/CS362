import unittest
import average_elements

class TestElements(unittest.TestCase):

    def test_sum(self):

        self.assertEqual(average_elements.ave_elements([2, 4, 6]), 4)

    def if_valid(self):

        self.assertEqual(average_elements.ave_elements([a, b, c]), "Invalid input.")

    def if_no_input(self):

        self.assertEqual(average_elements.ave_elements([]), "No inputs.")

if __name__ == '__main__':

    unittest.main()