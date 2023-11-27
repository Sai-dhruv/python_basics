from threading import *

class Test:
    def display(self):
        for i in range(10):
            print("From child thread")

obj = Test()
t = Thread(target=obj.display())
t.start()

for j in range(10):
    print("From main Thread ..")