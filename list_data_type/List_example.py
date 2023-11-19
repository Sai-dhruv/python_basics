import sys

# List is Mutable object
l = [] # Using square brackets we can create the list 
print(type(l))

l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(10)
l.append(None) # None alloed
print("List values :", l) # Order is preserved and duplicated allowed
print(l[0]) # Access using index value 
print(l[0:4]) # Using slice
l.remove(20) # Remove the value from list
print("List values after removeing 20 : ",l)
print(l[-1]) # Negative index access
print(" '*' Operator applicable for list :", l*2) # two times printed
print("Memory Size of the List :", sys.getsizeof(l))


