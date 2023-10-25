#!/usr/bin/env python3
"""
Simple helper function
"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            pass
    
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """Calculate the start index"""
        start_index = (page - 1) * page_size

        """Calculate the end index"""
        end_index = start_index + page_size

        return (start_index, end_index)
    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get page Simple pagination
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        dataset = self.dataset()
        start, end = self.index_range(page, page_size)
        if end > len(dataset):
            return []
        return [list(dataset[row]) for row in range(start, end)]