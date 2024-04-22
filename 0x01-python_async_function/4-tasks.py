#!/usr/bin/env python3
"""The code is nearly identical to wait_n except
task_wait_random is being called"""

import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """a function that will spawn wait_random n times"""
    spawn_task = []
    delays = []

    for i in range(n):
        task = task_wait_random(max_delay)
        spawn_task.append(task)

    for task in asyncio.as_completed((spawn_task)):
        delay = await task
        delays.append(delay)

    return delays
