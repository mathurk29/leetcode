
import threading
from time import sleep

def sleeper():
    current_thread = threading.get_ident()
    for i in range(5):
        print(i, current_thread)
        sleep(1)

t1 = threading.Thread(target=sleeper)
t2 = threading.Thread(target=sleeper)
t1.start()
t2.start()

for i in range(3):
    print(i, threading.current_thread().name)
    sleep(1)
