# PROJECT AUHOR :  ODIONYE OBIAJULU WILLIAMS
# PROJECT ITLE : Pagination

The content of this project are tasks for learning to paginate data.

Completed Tasks
Task 0: Simple Helper Function

    File: 0-simple_helper_function.py
    Description: This file contains a Python function called index_range which takes two integer arguments page and page_size. It returns a tuple of size two containing the start index and end index corresponding to the range of indexes for a given pagination. Page numbers are 1-indexed, meaning the first page is represented as page 1.

Task 1: Simple Pagination

    File: 1-simple_pagination.py
    Description: This file contains a Python script fulfilling the following requirements:
        It copies the index_range function from the previous task and includes a class named Server.
        The Server class is designed to paginate a database of popular baby names stored in a CSV file.
        The class includes a method named get_page, which takes two integer arguments: page (default value: 1) and page_size (default value: 10).
        The method utilizes assert to verify that both arguments are integers greater than 0.
        It uses the index_range function to find the correct indexes for pagination and returns the appropriate page of the dataset as a list of rows. If the input arguments are out of range for the dataset, an empty list is returned.

Task 2: Hypermedia Pagination

    File: 2-hypermedia_pagination.py
    Description: This file contains a Python script meeting the following requirements:
        It replicates code from the previous task.
        It implements a method named get_hyper in the Server class. This method takes the same arguments as get_page and returns a dictionary containing key-value pairs such as page_size, page, data, next_page, prev_page, and total_pages.
        The implementation reuses the get_page method. The math module can be used if necessary.

Task 3: Deletion-Resilient Hypermedia Pagination

    File: 3-hypermedia_del_pagination.py
    Description: This file contains a Python script satisfying the following requirements:
        It addresses the issue where certain rows might be removed from the dataset between two queries, ensuring that users do not miss items when changing pages.
        It begins with the provided code framework including the Server class for pagination of a database of popular baby names.
        It implements a method named get_hyper_index within the Server class. This method takes two integer arguments: index (default value: None) and page_size (default value: 10).
        The method returns a dictionary containing key-value pairs representing the current start index of the return page, the next index to query with, the current page size, and the actual page of the dataset. Assertions are used to verify that the index is in a valid range.
        The implementation ensures that even if rows are deleted from the dataset between queries, users receive the correct dataset page based on the specified index and page size.
