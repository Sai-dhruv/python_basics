from threading import *

l = RLock()
print("Main thread is going to acquire the lock")
l.acquire()
print("Main thread is going to acquire the lock again")
l.acquire()
print("Main thread same lock ")
