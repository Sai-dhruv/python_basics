a = 10
b = 10
print(id(a))
print(id(b))
print(id(a) == id(b)) # So both the address same in the case of int

c = 10.0
d = 10.0
print(id(c) == id(d)) # 