#!/usr/bin/env python3
"""
Helper function for index_range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function to take 2 int args and returns a tuple of size two
    with start and end index corresponding to index range
    indexes to return in a list for the pagination
    Args:
        page (int): page num to return (pages are 1-indexed)
        page_size (int): num of items on a page
    Return:
        tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
