### multithreading 
### when to use multithreading 
    ### I/O bound tasks: Tasks that spend more time waiting for I/O operations (e.g. file operations,network requests)

    ### concurrent execution : when you want to improve the throughput of your application by perfroming multiple operations 
    
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"NUMBER:{i}")
        
def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"letter:{letter}")

## create two threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)
## when one is sleeping other executes

t = time.time()
## start the thread
t1.start()
t2.start()

## wait for the threads to complete
t1.join()
t2.join()

finished_time = time.time() - t
print(finished_time)