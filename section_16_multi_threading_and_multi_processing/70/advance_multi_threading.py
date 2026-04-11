### Multithreading with thread pool executor

# A thread pool in Python is a collection of worker threads that can be reused to execute tasks concurrently. Using a thread pool is generally more efficient than manually creating new threads for each task because it reduces the overhead of thread creation and destruction.

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"NUMBER : {number}"

numbers = [1,2,3,4,5,6,7,8,9,0,1,2,3]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number,numbers)
    
for result in results:
    print(result)