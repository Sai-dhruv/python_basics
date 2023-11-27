from Person import Person
from Car import Car

class Employee(Person):
    c = Car()

    def __init__(self):
        print("I am from init method in Employee class")

    def code(self):
        print("Employee can code the functionality ..")



e = Employee()
e.code()
e.c.drive()
    
    
        