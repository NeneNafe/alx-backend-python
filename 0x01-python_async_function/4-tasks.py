#!/usr/bin/env python3
"""The code is nearly identical to wait_n except
task_wait_random is being called"""

import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """a function that will spawn wait_random n times"""
    spawn = []
    delays = []
    for i in range(n):
        delayed_task = task_wait_random(max_delay)
        delayed_task.add_done_callback(lambda x: delays.append(x.result()))
        spawn.append(delayed_task)

    for sp in spawn:
        await sp

    return delays
