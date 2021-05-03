import unittest
import volumeCube

class VolumeTest(unittest.TestCase):

    def number_test(self):

        self.assertEqual(volumeCube.volume_calc(1, 2, 3), 6)
    
    def dec_test(self):

        self.assertEqual(volumeCube.volume_calc(1.7, 2.8, 3.9), 18.564)

    def invalid_test(self):

        self.assertEqual(volumeCube.volume_calc(a, 2, -3), "Invalid input.")

if __name__ == '__main__':

    unittest.main()