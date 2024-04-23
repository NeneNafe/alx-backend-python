#!/usr/bin/env python3
"""a coroutine called async_generator that takes no arguments"""

import random
import asyncio


async def async_generator():
    """Takes no args but loops 10 times by picking a random number
    between the numbers 0 - 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
