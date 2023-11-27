from threading import *
import time

def wish(name):
    for i in range(10):
        print("Good morning  :", end='')
        time.sleep(2)
        print(name)

t = Thread(target=wish, args=("sai",))
t1 = Thread(target=wish, args=("niha",))
t.start()
t1.start()
