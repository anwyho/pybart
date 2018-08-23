from .context import pybart

import unittest
from pybart import *

class TestPybart(unittest.TestCase):

    def setUp(self):
        print(pybart)
        print(BART_KEY)
        pybart.updateStations.updateStations()
        
        # self.assertNotEqual(pybart.BART_KEY, None)

    def test_numbers_3_4(self):
        self.assertEqual(3*4, 12)

if __name__ == '__main__':
    unittest.main()