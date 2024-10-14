#!/usr/bin/env python3
"""The basics of async"""
import asyncio
import random


async def wait_random(wait_time: int = 10) -> float:
    """wait_random Function"""
    waiting = random.uniform(0, wait_time)
    await asyncio.sleep(waiting)
    return waiting
