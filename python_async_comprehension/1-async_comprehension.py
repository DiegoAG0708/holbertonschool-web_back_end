#!/usr/bin/env python3
"""
Module 1-async_comprehension
Provides a coroutine that collects 10 random numbers
using an async comprehension over async_generator.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using async comprehension.

    Returns:
        List[float]: A list of 10 random float values.
    """
    return [i async for i in async_generator()]
