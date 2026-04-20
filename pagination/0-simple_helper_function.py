#!/usr/bin/env python3
"""
Simple helper function
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing a start index and an end index
    for pagination parameters.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
