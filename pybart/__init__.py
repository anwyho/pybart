#!/bin/python3.6

__author__="Anthony W. Ho"

from .session import PybartSession

# TODO: Add version tuple
# Also, see Zappa __init__.py

# Key provided by BART API
DEFAULT_KEY='MW9S-E7SL-26DU-VV8V'

def pybartSession(api_key=DEFAULT_KEY):
    return PybartSession(api_key=api_key)

if __name__ == "__main__":
    print("Hello, BART!\nStatus: In Development")