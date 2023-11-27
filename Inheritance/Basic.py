class X:
    a=10
    def m1(self):
        print("Parent class Instance Method...")

    @classmethod
    def m2(cls):
        print("Parent class - class method..")

    @staticmethod
    def m3():
        print("Parent class static method..")  

    def __init__(self):
        self.b = 888
        print("Constructor Created from parent ...")  

    def __del__(self):
        print("Parent destructor ...")            

class Y(X):
    a= 99 # first priority
    def __init__(self):
        super().m3()
        self.d = 100
        print(self.__dict__)
    pass

y = Y()
print(y.a)
y.m1()
y.m2()
y.m3()
#print("Parent class instance variable :",y.b)