import unittest
import calc

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,5), 15)

    def test_add_2(self):
        self.assertEqual(calc.add(10,5), 4)

if __name__ == '__main__':
    unittest.main()