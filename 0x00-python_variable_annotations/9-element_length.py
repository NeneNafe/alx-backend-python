#!/usr/bin/env python3
"""An annotations func that takes an argument and return a list"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """lst is an function that has list"""
    return [(i, len(i)) for i in lst]
