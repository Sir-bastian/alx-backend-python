#!/usr/bin/env python3
'''Task 0: The basics of async
Write an asynchronous coroutine that takes in an integer
arg  ('max_delay', with a default value of 10) named 'wait_random'
that awaits for a random delay between 0 and 'max_delay'
(included and float value) second & eventually returns it.

Use the rnadom modelue.'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''waits for a random number of seconds'''
    wait_seconds: float = random.random() * max_delay
    await asyncio.sleep(wait_seconds)
    return wait_seconds
