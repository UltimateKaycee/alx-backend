#!/usr/bin/env python3
""" Module for BaseCaching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Class for a FIFO cache
    """

    def __init__(self):
        """
        Function to iInitialize class parent's init method
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Function to cache key-value pair
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usage[-1]))
                del self.cache_data[self.usage[-1]]
                del self.usage[-1]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Function to return value for a given key
        """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            return self.cache_data[key]
        return None
