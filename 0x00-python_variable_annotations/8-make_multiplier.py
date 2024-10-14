#!/usr/bin/env python3
""" Basic Annotations"""

from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier function"""
    def multiply(x: float) -> float:
        """multiply function"""
        return x * multiplier
    return multiply
