a=10
def f1():
    print("Global Variable a =", a)


f1()   
print(f1.__globals__)