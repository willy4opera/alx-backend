#!/usr/bin/env python3

'''The basic caching module.
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Here, we represented an object that allows the storing and
    retrieving of items from a dictionary.
    '''
    def put(self, key, item):
        '''Here, we add an item in the cache.
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''Fetches an item by key.
        '''
        return self.cache_data.get(key, None)
