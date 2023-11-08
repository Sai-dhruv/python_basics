def smartDivison(func):
    def inner(a,b):
        if b ==0:
            print("b Should not be zero")
        else:
            return func(a,b)
    return inner        

@smartDivison
def divison(a,b):
    return a/b

print(divison(10,2))
print(divison(10,0))