def isEven(x):
    if x%2 == 0:
        return True
    else:
        return False
l= [10,11,12,13,14,15,16]
f = type(filter(isEven,l))
print("Type of F ", f)
filterData = filter(isEven,l)
l1 = list(filterData)
print(l1)    