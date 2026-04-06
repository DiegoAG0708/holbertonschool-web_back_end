#!/usr/bin/env python3
"""
Module 6-sum_mixed_list
Provides a type-annotated function to sum a list
containing both integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Compute the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of numbers to sum.

    Returns:
        float: The total sum of the numbers in the list.
    """
    return sum(mxd_lst)
