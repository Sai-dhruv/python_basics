import sys

class Test:
    def __init__(self):
        print("Object created")

t1 = Test()
t1 = Test()
t3 = Test()
print("no of ref count ",sys.getrefcount(t1))        
