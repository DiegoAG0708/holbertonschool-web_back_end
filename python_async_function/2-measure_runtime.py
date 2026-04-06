#!/usr/bin/env python3
"""
Module 2-measure_runtime
Provides a function to measure the average runtime
of executing wait_n concurrently.
"""

import asyncio
import time
from typing import Union
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time of wait_n.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: The average time per coroutine.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
