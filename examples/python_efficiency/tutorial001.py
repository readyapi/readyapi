import itertools
from readyapi import ReadyAPI

app = ReadyAPI()

def demo_generators():
    print("1. Generators for Memory Efficiency")
    # List comprehension: memory-intensive
    my_list = [i * 2 for i in range(10**6)]
    print(f"List comprehension: {my_list[:3]} ... {my_list[-3:]}")
    # Generator expression: memory-efficient
    my_generator = (i * 2 for i in range(10**6))
    print(f"Generator expression: {list(itertools.islice(my_generator, 3))} ... (rest lazily generated)")
    print("-" * 50)
