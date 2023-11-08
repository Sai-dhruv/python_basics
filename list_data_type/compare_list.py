l = [10,20,30,40,50]
l2 = [10,20,30,40,50]

print(id(l))
print(id(l2)) # Both the values are same but address is different
print(l is l2) # False
print(l == l2) # True
l2.append(None)
print(l == l2)
