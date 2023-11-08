#without Map 
def double(x):
    return 2*x

l =[1,2,3]
l1 = list(map(double,l))
print(l1)

# With lambda
l2 = list(map(lambda x: 2*x,l))
print("Double value ",l2)

# With double 
l3 = list(map(lambda x,y: x*y, l1,l2 ))
print("L3 Value :", l3)