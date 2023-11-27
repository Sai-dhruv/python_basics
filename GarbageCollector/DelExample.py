import time

class DelExample:
    def __init__(self):
        print("Object initialization")

    def __del__(self):
        print('__del__ called - perform the clean up activities- before executing GC..!')

t1 = DelExample()
t1 = None
time.sleep(5)
print(" End of the application..")
