#!/usr/bin/env python3
'''Task 1: Let's execute multiple coroutines
at the same time with async'''
import asyncio
from typing import List


wait_random = __import__("0-basic_asnc_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''return the list of all the delays (float values)'''

    wait_time = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(wait_time)
