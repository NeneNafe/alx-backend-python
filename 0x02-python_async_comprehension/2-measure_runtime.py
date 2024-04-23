#!/usr/bin/env python3
"""a measure_runtime coroutine that will execute async_comprehension four times
in parallel using asyncio.gather"""

import asyncio
import random
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """executes async_comprehension four times in parallel
    using asyncio.gather"""
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.time()
    return end_time - start_time
