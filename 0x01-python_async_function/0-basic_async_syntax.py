#!/usr/bin/env python3
"""A function that is asynchronous"""

import random
import asyncio


async def wait_random(max_delay: float = 10.0) -> float:
    """an asynchronous coroutine that takes in an integer argument

    Args:
        max_delay (int): The argument
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
