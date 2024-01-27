#!/usr/bin/env python3
"""
File: 0-simple_helper_function.py

Function:
--------
def index_range(page, page_size):

The function should return a tuple of size two containing a start
index and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters.
"""
from typing import Tuple


def index_range(page: int, page_size:  int) -> Tuple:
    """
    parameters:
    - page (int): Current page number
    - page_size (int): Size of a page

    Returns:
    - (Tuple): A tuple of size two containing a start index and an end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
