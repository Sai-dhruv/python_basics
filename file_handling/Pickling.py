import pickle

class Employee:
    def __init__(self,eno,ename,esal,eadd):
        self.employee_number = eno
        self.employee_name = ename
        self.employee_sal = esal
        self.employee_address = eadd

    def display(self):
        print(self.employee_number, "\t", self.employee_name, "\t", self.employee_address)    

list = []
e = Employee(1,'Saikrishna',10000,'Plano')
list.append(e)
e = None
e = Employee(2,'Niharika',10000,'Plano')
list.append(e)
e = None
e = Employee(3,'Dhruv',100000,'Plano')
list.append(e)
e.display()

with open("emp.dat", "wb") as f:
    pickle.dump(e,f)
    print("Pickling of employee is completed ...")
with open("emp.dat", "rb") as f:    
    obj = pickle.load(f)
    obj.display()
