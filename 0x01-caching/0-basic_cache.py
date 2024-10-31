#!/usr/bin/env python3
""" module for basecashing
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class for caching info in key-value pairs
    Methods:
        put(key, item) - key-value pair
        get(key) - retrieve value associated with key
    """

    def __init__(self):
        """
        Function to initialize class with parent method __init__
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Function to store key-value pair
        Args:
            Key
            Item
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Function to return value for key.
        If no key, return None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
