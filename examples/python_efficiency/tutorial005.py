import itertools
import time

from readyapi import ReadyAPI

app = ReadyAPI()


@app.get("/efficiency/efficient_loops")
async def efficient_loops_demo():
    """
    Endpoint demonstrating efficient looping techniques,
    comparing itertools.chain, map, and list comprehensions.
    """
    # itertools.chain example
    a = [1, 2, 3]
    b = [4, 5, 6]
    chained = list(itertools.chain(a, b))

    # map vs list comprehension timing
    data = range(10**6)
    start = time.time()
    map_res = list(map(lambda x: x * 2, data))
    map_time = time.time() - start

    start = time.time()
    list_comp_res = [x * 2 for x in data]
    list_comp_time = time.time() - start

    return {
        "itertools_chain_result": chained,
        "map_time_sec": round(map_time, 4),
        "list_comprehension_time_sec": round(list_comp_time, 4),
        "note": (
            "itertools can be more memory-efficient for chaining iterables, "
            "and map() can be slightly faster than a list comprehension for large data."
        ),
    }
