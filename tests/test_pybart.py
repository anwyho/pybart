from .context import pybart

import os
import unittest
from pybart import *

class TestPybart(unittest.TestCase):

    def setUp(self):
        key = os.environ['BART_PRIV']
        session = pybart.session(api_key=key)
        self.assertNotEqual(session.key, None)

    def test_passing(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()