#!/usr/bin/env python3
""" FIFO caching """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Caching system """
    def __init__(self):
        """ Initialize """
        super().__init__()

    def put(self, key, item):
        """
        - Inserts to a dictionary or to a cache.
        - If the size is greater that the cache can store,
          it will evict the first chached value in FIFO algorithm.
        """
        if key is None or item is None:
            return None
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item = next(iter(self.cache_data))
            del self.cache_data[first_item]
            print(f"DISCARD: {first_item}")

    def get(self, key):
        """
        Returns the value that is linked to the key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
