class Student:
    # Here I am writing doc String
    ''' This is Student Data'''
    def __init__(self,name,rollNo,marks):
        self.name = name
        self.rollNo = rollNo
        self.marks = marks

    def display(self):
        print("Student rollNumber = {}   name ={} marks ={}   ".format(self.rollNo,self.name,self.marks))

s1 = Student('sai',10,100)
s1.display()
help(s1)