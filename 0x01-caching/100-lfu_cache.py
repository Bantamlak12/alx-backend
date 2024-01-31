#!/usr/bin/env python3
""" LFU Caching """
from collections import OrderedDict, defaultdict

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Caching system """
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequecy = defaultdict(int)

    def put(self, key, item):
        """ Inserts item to the cache with LFU caching algorithm """
        if key is None or item is None:
            return None

        # If the key is in the cache, update it
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequecy[key] += 1
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            key_min_frequency = min(self.frequecy, key=self.frequecy.get)
            del self.cache_data[key_min_frequency]
            del self.frequecy[key_min_frequency]
            print(f"DISCARD: {key_min_frequency}")
        self.cache_data[key] = item
        self.frequecy[key] += 1

    def get(self, key):
        """ Returns the value related to the key """
        if key is None or key not in self.cache_data:
            return None
        self.frequecy[key] += 1
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
