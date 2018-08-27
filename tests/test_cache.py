import pybart

import os
import unittest

class TestCache(unittest.TestCase):
    def setUp(self):
        self.key = os.environ['BART_PRIV']
        self.cache = pybart.cacheOps.Cache()

    def test_passing(self):
        
        self.assertTrue(True)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()