import time

class DelExample:
    def __init__(self):
        print("Object initialization")

    def __del__(self):
        print('__del__ called - perform the clean up activities- before executing GC..!')

t1 = DelExample()
t2 = t1
del t1
print("t1 deleted but Object not destroyed..")
t3 = t2
del t2
print("t2 deleted but object not destroyed")
time.sleep(5)
print("Object is going to destroy... ")
del t3
print(" End of the application..")

#if the ref is there then object will not eligible for GC