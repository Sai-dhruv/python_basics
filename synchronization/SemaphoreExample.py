from threading import *
import time
s= Semaphore(3) # we can assign fixed number of threads
def wish(name):
    s.acquire()
    for i in range(5):
        print('Good Morning ', end='')
        time.sleep(2)
        print(name)
    s.release()

t1 = Thread(target=wish, args=("A",))
t2 = Thread(target=wish, args=("B",))
t3 = Thread(target=wish, args=("C",))
t4 = Thread(target=wish, args=("D",))
t1.start()
t2.start()
t3.start()
t4.start()