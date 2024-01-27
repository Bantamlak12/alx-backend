#!/usr/bin/env python3
"""
File: 0-simple_helper_function.py

Function:
--------
def index_range(page, page_size):

The function should return a tuple of size two containing a start
index and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters.

Note:
- Page numbers are 1-indexed, i.e. the first page is page 1

- If you are on page 3 with a page size of 15, it means your looking at the 3rd
subset/page of 15 elements from the larger dataset.
"""
from typing import Tuple


def index_range(page: int, page_size:  int) -> Tuple:
    """
    parameters:
    - page (int): subset or page of the entire dataset.
    - page_size (int): Number of elements that are displayed on a single page.

    Returns:
    - (Tuple): A tuple of size two containing a start index and an end index.
    - The start index is the starting position of the first element
      in the currrent page.
    - The end index is the end position of the last element.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
