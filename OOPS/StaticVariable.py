class Student:
    ''' Staic method is here in this clss'''
    cname = "MallaReddy Engineering college"

s = Student()
print(s.cname)
print(Student.cname) # Recomended .. Static variable should access using class name     