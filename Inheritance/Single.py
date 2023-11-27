class A:
    def __init__(self):
        print("I am from init in class A")

    def m1(self):
        print(" I am from m1 method in class A ")

class B(A):
    def __init__(self):
        print("I am from init method in B class")

    def m2(self):
        print(" I am from m2 method in class B")

b = B()
b.m1()            
