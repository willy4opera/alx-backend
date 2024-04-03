#!/usr/bin/env python3

'''The most Recently Used caching module.
'''
from collections import OrderedDict

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''Here, we represents the object that allows the storing and
    retrieval of items from a dictionary with an MRU
    removal mechanism when the limit is reached.
    '''
    def __init__(self):
        '''Cache initialization.
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Add item to the cache.
        '''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''Fetch item by key.
        '''
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
