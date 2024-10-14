#!/usr/bin/env python3
""" Basic Annotations"""

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv function"""
    return (k, v ** 2)
