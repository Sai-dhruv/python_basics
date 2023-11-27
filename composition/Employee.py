from Car import Car

class Employee:
    def __init__(self,id,name,car):
        self.id = id
        self.name = name
        self.car = car

    def getEmpInfo(self):
        print("Employee name {} and car Name {}".format(self.name, self.car.carName))
        self.car.getCarInfo()

c = Car("Nissan","SV")
e = Employee(1,"Sai",c)
e.getEmpInfo()
