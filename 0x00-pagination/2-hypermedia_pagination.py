#!/usr/bin/env python3

"""2. The Hypermedia pagination sample.
"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.
    """
    begin = (page - 1) * page_size
    last = begin + page_size
    return (begin, last)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance.
        """
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
        """Fetches a page of data.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        begin, last = index_range(page, page_size)
        data = self.dataset()
        if begin > len(data):
            return []
        return data[begin:last]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Fetches information about a page.
        """
        page_data = self.get_page(page, page_size)
        begin, last = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if last < len(self.__dataset) else None,
            'prev_page': page - 1 if begin > 0 else None,
            'total_pages': total_pages,
        }
        return page_info
