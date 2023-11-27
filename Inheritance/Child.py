from Parent import Parent 

class Child(Parent):
    def __init__(self):
        print("Child object Created")

    def m3(self):
        print(" I am from child me method")

c = Child()
c.m1()            
    