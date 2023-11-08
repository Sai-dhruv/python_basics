def outer():
    print("Outer Function calling")
    def inner():
        print("Inner Function called..")
    print("Outer function returning Inner function")
    return inner

f1 = outer()
print("Print :", f1)    
        