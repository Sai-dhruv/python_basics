class Parent:
    a = 999
    def m1(self):
        b = 10
        print("I am from parent M1 method")

class child(Parent):
    def __init__(self):
        print("From child init method ...")
    def m2(self):
        print("I am from child class m1 Method")
        print("Trying to access 'b' in parent call using super ..")#AttributeError: 'super' object has no attribute 'b'
       # print(super().b)
        print("Access parent class static method using 'self' ")
        print(self.a)    

c = child()
c.m1()
c.m2()
