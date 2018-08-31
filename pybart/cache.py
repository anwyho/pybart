import json
import os
import time
import sys

# class for accessing local cache or aws s3 bucket
class Cache:
    def __init__(self):
        pass

    def retrieve_json(self, stnsFilename, cacheDir='.', forceRefresh=False):
        cachedPath = cacheDir + stnsFilename
        DAYS = 60*60*24  # seconds
        # cached file is at least 7 days old
        if forceRefresh or time.time()-os.stat(cachedPath).st_atime >= 7*DAYS:
            # TODO: Refresh cached file
            pass
        else: 
            try:
                with open(cachedPath) as f:
                    res = json.load(f)
            except json.decoder.JSONDecodeError as j:
                print(j)
            except Exception as e:
                print("Failed to open and write to given cache file {cacheDir} with error: {e}".format(cacheDir=cacheDir,e=e), file=sys.stderr)

                # retry calling api if load failed
        
class LocalCache(Cache):
    def __init__(self):
        pass

class S3Cache(Cache):
    def __init__(self):
        pass
