from __future__ import print_function

from . import updateStations

import json
import os
import requests
from sys import argv

try:
    PUBL_KEY=os.environ['BART_PUBL']
    PRIV_KEY=os.environ['BART_PRIV']
except KeyError as e:
    raise Exception("ERROR: Missing BART API key.")

BART_KEY=PUBL_KEY


class Pybart:
    def __init__(self): 
        self.key = BART_KEY


if __name__ == "__main__":
    print("Hello, BART!\nStatus: Ready")