#!/usr/bin/env python3
""" Basic dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Caching system """
    def __init__(self, ):
        """
        Initialize with super()
        """
        super().__init__()

    def put(self, key, item):
        """ Assigns to a dictionary """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Returns the value in self.cache_data linked to key """
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
