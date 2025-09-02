from collections import deque
from readyapi import ReadyAPI

app = ReadyAPI()

@app.get("/efficiency/deque")
async def deque_demo():
    """
    Endpoint demonstrating the efficiency of collections.deque for fast appends and pops.
    """
    # List: slow insert at the beginning (O(n))
    my_list = [1, 2, 3]
    my_list.insert(0, 0)
    list_result = my_list.copy()

    # Deque: fast appendleft and popleft (O(1))
    my_deque = deque([1, 2, 3])
    my_deque.appendleft(0)
    popped = my_deque.popleft()
    deque_result = list(my_deque)

    return {
        "list_after_insert": list_result,
        "deque_after_appendleft_and_popleft": deque_result,
        "popped_from_deque": popped,
        "note": "Deque allows fast O(1) insertions/removals at both ends, unlike lists."
    }
