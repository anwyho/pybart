import pybart

import os
import unittest

class TestSession(unittest.TestCase):
    def setUp(self):
        self.key = os.environ['BART_PRIV']
        self.session = pybart.pybartSession(api_key=self.key)

    def test_key_switch(self):
        oldKey = self.session.key
        self.session.key = os.environ['BART_PUBL']
        self.assertNotEqual(oldKey, self.session.key)


if __name__ == '__main__':
    unittest.main()