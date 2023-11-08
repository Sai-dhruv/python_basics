s = 'Saikrishna'
a = "Saikrishna"
print(s[0:3]) # Sai
print(s[-7:]) # krishna
print(s[:]) # Saikrishna
print(len(s))

print(id(a)," --", id(s))
print(s is a) # Address comparison 

print(s == a ) # Content comparison

print(s == a[1:]) # False