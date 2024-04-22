#!/usr/bin/env python3
"""A function that is asynchronous"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """an asynchronous coroutine that takes in an integer argument

    Args:
        max_delay (int): The argument
    """
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
