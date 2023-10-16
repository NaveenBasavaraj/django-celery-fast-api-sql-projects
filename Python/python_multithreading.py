import threading, time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

def do_something(seconds):
    print(f"sleep for {seconds} seconds")
    time.sleep(seconds)
    print("done...")

# start = time.perf_counter()
# with ThreadPoolExecutor() as tpe:
#     results = [tpe.submit(do_something, 1) for _ in range(10)]
    
#     for f in as_completed(results):
#         print(f.result())
    

# end = time.perf_counter()
# print(f"total time {end-start} seconds")


start = time.perf_counter()
with ProcessPoolExecutor() as tpe:
    results = [tpe.submit(do_something, 1) for _ in range(10)]
    
    for f in as_completed(results):
        print(f.result())
    

end = time.perf_counter()
print(f"total time {end-start} seconds")
