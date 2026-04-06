#!/usr/bin/env python3
"""
Module 3-tasks
Provides a function that creates an asyncio.Task
to run the wait_random coroutine.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for wait_random.

    Args:
        max_delay (int): Maximum delay for wait_random.

    Returns:
        asyncio.Task: A task running wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
