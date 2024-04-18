#!/usr/bin/env python3
from typing import List
"""a type-annotated function sum_list which takes a list input_list
of floats as argument and returns their sum as a float"""


def sum_list(input_list: List[float]) -> float:
    """takes a list of floats as arguments

    Args:
        input_list (float): the list of floats

    Returns:
        float: the sum of the list of floats
    """
    return sum(input_list)
