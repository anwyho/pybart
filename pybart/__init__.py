from __future__ import print_function

from . import updateStations

import json
import os
import requests
from sys import argv

DEFAULT_KEY='MW9S-E7SL-26DU-VV8V'

class session:
    def __init__(self, api_key=DEFAULT_KEY, cache_dir=None):
        self._key = api_key
        self._cache_dir = cache_dir

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, new_key):
        self._key = new_key


    # TODO: migrate updateStations to here
    # TODO: change name of updateStations
    def updateStations(self):
        pass


if __name__ == "__main__":
    print("Hello, BART!\nStatus: Ready")