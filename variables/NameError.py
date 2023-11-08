def f1():
    a =10
    print("Local variable to F1 ",a)

def f2():
   # print("Name Error Here ",a) #NameError: name 'a' is not defined
   pass 
f1()
f2()    
