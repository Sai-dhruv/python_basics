from threading import *
import time

e = Event()
def consumer():
    print('COnsumer thread waiting for notification ...') # 1
    e.wait()
    print('COnsumer thread got the notification ... ')#4

def producer():
    time.sleep(5)
    print('Producer thread producing items ') #2
    print('Giving notification by setting EVent ') #3
    e.set()

t1 = Thread(target=producer)
t2 = Thread(target=consumer)
t1.start()
t2.start()        