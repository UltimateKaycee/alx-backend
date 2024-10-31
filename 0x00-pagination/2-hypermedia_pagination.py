#!/usr/bin/env python3
"""
Module with methods to create pagination from csv data
"""
import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Class to paginate popular baby names database.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Function to access csv file and return dataset.
        Returns:
            List[List]: Dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def assert_positive_integer_type(value: int) -> None:
        """
        Function to show value is a +ve int.
        Args:
            value (int): Value to show.
        """
        assert type(value) is int and value > 0

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Function to returns dataset page.
        Args:
            page (int): Page num.
            page_size (int): Page size.
        Returns:
            List[List]: Dataset page.
        """
        self.assert_positive_integer_type(page)
        self.assert_positive_integer_type(page_size)
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        try:
            data = dataset[start:end]
        except IndexError:
            data = []
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns dataset page.
        Args:
            page (int): page num.
            page_size (int): page size.
        Returns:
            List[List]: Dataset page.
        """
        total_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        info = {
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "total_pages": total_pages,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= total_pages else None
        }
        return info
