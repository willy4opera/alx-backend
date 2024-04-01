#!/usr/bin/env python3

""" 2. Hypermedia pagination.
"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ the index range from a given page and page size.
    """
    begin = (page - 1) * page_size
    end = begin + page_size
    return (begin, end)


class Server:
    """Server class to that paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes new Server instance.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """The cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                re_reader = csv.re_reader(f)
                dataset = [row for row in re_reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Fetches the page of data.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        begin, end = index_range(page, page_size)
        data = self.dataset()
        if begin > len(data):
            return []
        return data[begin:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Fetches information about a page.
        """
        pg_date = self.get_page(page, page_size)
        begin, end = index_range(page, page_size)
        total_pgs = math.ceil(len(self.__dataset) / page_size)
        page_info = {
            'page_size': len(pg_date),
            'page': page,
            'data': pg_date,
            'next_page': page + 1 if end < len(self.__dataset) else None,
            'prev_page': page - 1 if begin > 0 else None,
            'total_pgs': total_pgs,
        }
        return page_info
