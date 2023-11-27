from threading import *

def display():
    print("I am from display method :", current_thread().getName())


t = Thread(target=display)
t.setName("Sai")
t.start()