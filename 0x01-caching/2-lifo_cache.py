#!/usr/bin/env python3
""" LIFO Caching """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Caching system """
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.last_updated_key = None

    def put(self, key, item):
        """
        - Inserts item  to the cache. If the key to be added is already
        in the cache, it updates itself with the new value.
        """
        if key is None or item is None:
            return None

        if key in self.cache_data:
            self.last_updated_key = key
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.last_updated_key:
                self.cache_data.pop(self.last_updated_key)
                print(f"DISCARD: {self.last_updated_key}")
            else:
                keys_reversed = list(reversed(list(self.cache_data)))
                last_item_key = keys_reversed[0]
                self.cache_data.pop(last_item_key)
                print(f"DISCARD: {last_item_key}")
        self.cache_data[key] = item
        self.last_updated_key = key

    def get(self, key):
        """
        - Returns a value related to the key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
