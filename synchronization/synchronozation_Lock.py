from threading import *
import time
l = Lock()
def wish(name):
    l.acquire()
    for i in range(10):
        print("Good morning  :", flush=True, end='')
        time.sleep(2)
        print(name)
    l.release()    
t = Thread(target=wish, args=("sai",))
t1 = Thread(target=wish, args=("niha",))
t.start()
t1.start()
