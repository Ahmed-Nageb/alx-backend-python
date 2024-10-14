#!/usr/bin/env python3
"""0-basic"""
import asyncio
import random


async def wait_random(wait_time=10):
    """wait_random Function"""
    waiting = random.uniform(0, wait_time)
    await asyncio.sleep(waiting)
    return waiting
