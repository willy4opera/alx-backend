#!/usr/bin/env python3

'''The Last-In First-Out caching module.
'''
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''Here, we represented an object that allows for thee storing and
    retrieval of items from a dictionary with a LIFO
    removal mechanism when the limit is reached.
    '''
    def __init__(self):
        '''cache initialization.
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Adding item in the cache.
        '''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        '''Fetches an item by key.
        '''
        return self.cache_data.get(key, None)
