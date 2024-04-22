#!/usr/bin/env python3
"""an async routine called wait_n that takes in 2 int arguments
You will spawn wait_random n times with the specified max_delay.
"""


import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """a function that will spawn wait_random n times"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    sorted_delays = [delay for delay in sorted(delays)]

    return sorted_delays
