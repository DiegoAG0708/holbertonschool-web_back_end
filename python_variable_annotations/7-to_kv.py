#!/usr/bin/env python3
"""
Module 7-to_kv
Provides a type-annotated function that returns a tuple
with a string and the square of an int or float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of a number.

    Args:
        k (str): The string key.
        v (Union[int, float]): The number to square.

    Returns:
        Tuple[str, float]: A tuple containing k and v squared as a float.
    """
    return (k, float(v ** 2))
