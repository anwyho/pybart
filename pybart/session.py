#!/bin/python3.6

__author__="Anthony W. Ho"

from . import cacheOps

import json
import os
import requests
import sys

class PybartSession:
    """
    something goes here
    """  # TODO: Complete this thing

    def __init__(self, 
            api_key=None):
        self._key = api_key
        self._cacheDir = None
        self._awsBucket = None
        self._awsDir = None

    @property
    def cacheDir(self):
        return self._cacheDir

    @cacheDir.setter
    def cacheDir(self, newDir):
        os.makedirs(os.path.dirname(newDir), exist_ok=True)
        self._cacheDir = os.path.dirname(newDir)

    @property
    def awsBucket(self):
        return self._awsBucket, self._awsDir

    @awsBucket.setter
    def awsBucket(self, newBucket, awsCacheDir):
        self._awsBucket = newBucket
        self._awsDir = awsCacheDir

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, new_key):
        self._key = new_key


    # TODO: migrate updateStations to here
    def refresh_stations(self, forceRefresh=False, useLocalCache=False, cacheDir=None):
        # json = cacheOps.retrieve_json()
        if self._cacheDir:
            try:
                stnsFilename = self._cacheDir + 'stns.json'
                os.stat(stnsFilename).ST_MTIME  # time last accessed

                with open(self._cacheDir + 'stns.json' "rb") as stns:
                    stations = json.load(stns)
            except json.decoder.JSONDecodeError as j:
                print(j)
            except Exception as _:
                print("Couldn't write to given cache directory {}."
                    .format(self._cacheDir),file=sys.stderr)
            
        # check for cached version
        # if cached
            # read from cache
            # report errors
        # else
            # use requests to call BART API
            # report errors
        # if cached
            # write to cache
        pass