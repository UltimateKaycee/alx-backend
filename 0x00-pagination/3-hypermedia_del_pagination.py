#!/usr/bin/env python3
"""
Module for Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Class to paginate popular baby names database.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Function for dataset indexed by sorting position from 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Function to take 2 int args and return a dictionary with
        key-value pairs:
            index: index of first item in page
            next_index: index of first item next page
            page_size: current page size
            data: page of dataset
        Args:
            index(int): first required index
            page_size(int): num of records per page
        """
        dataset = self.indexed_dataset()
        data_length = len(dataset)
        assert 0 <= index < data_length
        response = {}
        data = []
        response['index'] = index
        for i in range(page_size):
            while True:
                curr = dataset.get(index)
                index += 1
                if curr is not None:
                    break
            data.append(curr)

        response['data'] = data
        response['page_size'] = len(data)
        if dataset.get(index):
            response['next_index'] = index
        else:
            response['next_index'] = None
        return response
