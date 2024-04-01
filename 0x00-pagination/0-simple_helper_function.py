#!/usr/bin/env python3

""" The Index Pagination helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """The fuction gets the index range from a given
        page and page size.
    """
    begin = (page - 1) * page_size
    end = begin + page_size
    return (begin, end)
