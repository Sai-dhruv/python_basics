x = {} # This is not default set , It is a dict
print(type(x)) 

s = set()
print(type(s))
s.add("First one")
s.add('sai')
s.add(10)
s.add("Baby")
s.add('removable Variable')
print("set printing :",s)
s.pop() # removed first one
print("Afer poping :",s)
s.remove(10)
print("After Removing",s)