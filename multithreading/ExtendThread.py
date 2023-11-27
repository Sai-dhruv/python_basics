from threading import *

class Mythread(Thread):
    def run(self) :
        for i in range(10):
            print("Thread child ")

t = Mythread()
t.start()            
for j in range(10):
    print("Main thread ")
