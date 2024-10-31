#!/usr/bin/env python3
"""
Function for that paginates a database containing popular baby names
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function takes 2 int args to return a tuple with
    start and end index that corresponding to the range of
    indexes to return for pagination parameters
    Args:
        page (int): page num to return (pages are 1-indexed)
        page_size (int): num of items per page
    Return:
        tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)


class Server:
    """Class to paginate baby names database
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Function for cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Function takes 2 int args to return page from dataset
        Args:
            page (int): reqested page num - a positive int
            page_size (int): num of records on a page - a negative int
        Return:
            list of lists with data from the dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        dataset = self.dataset()
        data_length = len(dataset)
        try:
            index = index_range(page, page_size)
            return dataset[index[0]:index[1]]
        except IndexError:
            return []
