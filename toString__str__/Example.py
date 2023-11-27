class Student:
    def __init__(self,rollNumber,name):
        self.rollNumber= rollNumber
        self.name=name

    def __str__(self):
        return "Student name : {}  and roll Number : {}  ".format(self.name,self.rollNumber)    



s1 = Student(10,'saikrishna')
s2 = Student(20, "Niharika")
print(s1)
print(s2)