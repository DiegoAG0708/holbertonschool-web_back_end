#!/usr/bin/env python3
"""
Module 0-async_generator
Provides an asynchronous generator that yields random numbers
between 0 and 10 after waiting 1 second, repeated 10 times.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Yield random numbers between 0 and 10, 10 times.

    Each iteration waits asynchronously for 1 second before yielding.

    Returns:
        AsyncGenerator[float, None]: An async generator yielding floats.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
