from threading import *
import time

def consumer(c):
    c.acquire()
    print('COnsumer thread waiting state for update')
    count = '.'
    for i in range(5):
        count = count+'.'    
        print('waiting',count)
    c.wait()
    print('Consumer Got the notification ')
    c.release()

def producer(c):
    c.acquire()
    print('Producer producing the items ')
    print('Producer giving the Notification')
    time.sleep(5)
    c.notify()
    c.release()

c = Condition()
t1 = Thread(target=consumer, args=(c,))
t2 = Thread(target=producer, args=(c,))
t1.start()
t2.start()        