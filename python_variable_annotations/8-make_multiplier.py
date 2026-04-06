#!/usr/bin/env python3
"""
Module 8-make_multiplier
Provides a type-annotated function that returns
a multiplier function for floats.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns the product of that float and multiplier.
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func
