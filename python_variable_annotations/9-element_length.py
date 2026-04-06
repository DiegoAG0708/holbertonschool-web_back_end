#!/usr/bin/env python3
"""
Module 9-element_length
Provides a type-annotated function that returns
a list of tuples with elements and their lengths.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Compute the length of each element in an iterable of sequences.

    Args:
        lst (Iterable[Sequence]): The iterable containing sequence elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        the element and its length.
    """
    return [(i, len(i)) for i in lst]
