import gc
def add(a,b):
    return a+1,b+3

print(add(10,20))
s = add(1,2)
#print(s.index(1))
print(gc.isenabled())