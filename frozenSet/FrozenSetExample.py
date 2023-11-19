s = set()
s.add(10)
print(type(s))
fs = frozenset(s)
print(type(fs))
print("Frozen Set printing : ", fs) # tuple and Set is called frozenset

a = ({'hello'})
print("--------",type(a))