class Employee:
    def __init__(self,no,name,sal):
        self.eNumber = no
        self.eName = name
        self.eSal = sal

    def display(self):
        print("Number ",self.eNumber)
        print("Name ", self.eName)
        print("sal",self.eSal)

class Test:
    def modify(employee):
        employee.eSal = employee.eSal+100
        employee.display()

emp = Employee(1,'sai',100)
emp.display()
Test.modify(emp)        
