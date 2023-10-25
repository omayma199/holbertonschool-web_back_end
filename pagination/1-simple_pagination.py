#!/usr/bin/env python3
"""
Simple helper function
"""
import csv
import math
from typing import List, Tuple


index_range = __import__('0-simple_helper_function').index_range
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
        # Verify that both arguments are integers greater than 0
        if not (isinstance(page, int) and isinstance(page_size, int) and page > 0 and page_size > 0):
            return []

        # Get the total number of rows in the dataset
        total_rows = len(self.dataset())

        # Calculate the start and end indexes using the index_range function
        start_index, end_index = index_range(page, page_size)

        # Check if the page is out of range
        if start_index >= total_rows:
            return []
        # Slice the dataset to get the appropriate page
        page_data = self.dataset()[start_index:end_index]

        return page_data