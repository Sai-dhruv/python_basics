s = 'sai'
a = 'saikrishna'

print(s is a) # False > Address not same
print(s == a) # False > content not same

print(s == a[0:3]) # Now content same

x = 10 
y = 10
print(x is y) # True > Address same
print( x == y) # True > content same 

i = 300
j = 300
print(type(i))
print(id(i))
print(id(j))
print("Address comparion for x and Y : " , (i is j))