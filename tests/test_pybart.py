from .context import pybart

import unittest
import pybart

class TestPybart(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(3*4, 12)

if __name__ == '__main__':
    unittest.main()