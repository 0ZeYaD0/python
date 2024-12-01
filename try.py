from functools import *
import psutil
import os

class Test:
    def __init__(self, number):
        self.number = number

    def fip(self, number):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, number + 1):
            a, b = b, a + b
        return b

# Function to get the memory usage of the current process
def get_memory_usage():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss  # in bytes

# Example usage
print(f"Memory usage: {get_memory_usage() / (1024 * 1024):.2f} MB")

# Instantiate the class with a number
test_instance = Test(50)

for i in range(50):
    print(test_instance.fip(i))