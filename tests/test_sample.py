import unittest

class SampleTest(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(2*2, 4)

if __name__ == '__main__':
    unittest.main()
