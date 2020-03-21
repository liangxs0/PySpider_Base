import threading
import time

def target(second):
    print(f'Threading {threading.current_thread().name} is running')
    print(f'Threading {threading.current_thread().name} sleep {second}s')
    time.sleep(second)
    print(f'Threading {threading.current_thread().name} is ended')
threads = []
print(f'Threading {threading.current_thread().name} is running')
for i in [1,5]:
    thread = threading.Thread(target=target,args=[i])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print(f'Threading {threading.current_thread().name} is ended')

