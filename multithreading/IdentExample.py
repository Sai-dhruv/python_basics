from threading import *
def display():
    print("Child thread printing..")

t = Thread(target=display)
t.start()
print("Main thread identification number :",current_thread().ident)
print("child thread identification number : ",t.ident)       