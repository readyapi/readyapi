import math
import time
from readyapi import ReadyAPI

app = ReadyAPI()

@app.get("/efficiency/local_variable_lookup")
async def local_variable_lookup_demo():
    """
    Endpoint demonstrating the performance difference between
    global and local variable lookups in tight loops.
    """
    # Global lookup
    start_time = time.time()
    for _ in range(10**6):
        result = math.sqrt(25)
    global_lookup_time = time.time() - start_time

    # Local lookup
    local_sqrt = math.sqrt
    start_time = time.time()
    for _ in range(10**6):
        result = local_sqrt(25)
    local_lookup_time = time.time() - start_time

    return {
        "global_lookup_time_sec": round(global_lookup_time, 4),
        "local_lookup_time_sec": round(local_lookup_time, 4),
        "note": (
            "Using a local variable for frequently used functions inside hot loops "
            "can yield significant performance improvements in Python."
        )
    }
