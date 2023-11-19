class Student:
    def read(delf,a): # Delf also working but need write self always
        delf.name = a 

s = Student()
s.read('sai')    # No Need to pass self 
print(s.name)    