def f1():
    def inner(a,b):
        print("sum", a+b)
        print("Avg", (a+b)/2)
    inner(10,20)
    inner(20,23)

f1()        