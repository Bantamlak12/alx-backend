#!/usr/bin/env python3
""" LRU Caching """
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Caching system """
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Inserts an item to the cache using LRU algorithm """
        if key is None or item is None:
            return None
        if key in self.cache_data:
            self.cache_data[key] = item
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key, value = self.cache_data.popitem(last=False)
            print(f"DISCARD: {oldest_key}")
        self.cache_data[key] = item

    def get(self, key):
        """ Returns value linked to the key """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
