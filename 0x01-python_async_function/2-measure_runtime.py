#!/usr/bin/env python3
""" a measure_time function with integers n and max_delay as
arguments that measures the total execution time for wait_n(n,
max_delay), and returns total_time / n
"""


from asyncio import run
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures the total execution time for wait_n(n, max_delay)"""
    start_time = time()
    run(wait_n(n, max_delay))
    end_time = time()

    elapsed_time = end_time - start_time
    return elapsed_time / n
