#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the start index"""
    start_index = (page - 1) * page_size

    """Calculate the end index"""
    end_index = start_index + page_size

    return (start_index, end_index)
