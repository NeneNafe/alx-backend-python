#!/usr/bin/env python3
"""a function task_wait_random that takes an integer max_delay
and returns a asyncio.Task"""

import asyncio
from asyncio import create_task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """A function tht returns a text"""
    async def coro():
        await wait_random(max_delay)

    return create_task(coro())
