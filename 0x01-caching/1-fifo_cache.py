#!/usr/bin/env python3

'''The first-In first-Out caching module.
'''
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''Here, we represents an object that allows the storing and
    retrieval of items from a dictionary with a FIFO
    removal mechanism when the limit is reached.
    '''
    def __init__(self):
        '''Here, we initializes the cache.
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Here, we add an item in the cache.
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        '''Here, we retrieve the item by key.
        '''
        return self.cache_data.get(key, None)
