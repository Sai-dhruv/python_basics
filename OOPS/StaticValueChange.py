class Student:
    cname = "VVDC"
    def name(self):
        self.cname = "Viveka vardhani degree college"

s = Student()
print(Student.cname)
s.name()
print(s.cname)      
print(Student.cname)  