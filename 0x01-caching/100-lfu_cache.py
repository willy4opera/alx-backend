#!/usr/bin/env python3

'''The least Frequently Used caching module.
'''
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''Here, we represent an object that allows storing and
    retrieval of items from a dictionary with a LFU
    removal mechanism when the limit is reached.
    '''
    def __init__(self):
        '''Cache initialization.
        '''
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequent_kys = []

    def __reorder_items(self, mru_key):
        '''Reorders the items in this cache based on the most
        recently used item.
        '''
        maximum_pos = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0
        for i, key_freq in enumerate(self.frequent_kys):
            if key_freq[0] == mru_key:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(maximum_pos) == 0:
                maximum_pos.append(i)
            elif key_freq[1] < self.frequent_kys[maximum_pos[-1]][1]:
                maximum_pos.append(i)
        maximum_pos.reverse()
        for pos in maximum_pos:
            if self.frequent_kys[pos][1] > mru_freq:
                break
            ins_pos = pos
        self.frequent_kys.pop(mru_pos)
        self.frequent_kys.insert(ins_pos, [mru_key, mru_freq])

    def put(self, key, item):
        '''Add item to the cache.
        '''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.frequent_kys[-1]
                self.cache_data.pop(lfu_key)
                self.frequent_kys.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.frequent_kys)
            for i, key_freq in enumerate(self.frequent_kys):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.frequent_kys.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        '''Fetches an item by key.
        '''
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
