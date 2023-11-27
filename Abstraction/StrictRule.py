from abc import * 

class Vehicle(ABC):
    @abstractmethod
    def getNoOfWheels(self):
        pass

v = Vehicle()
print(v.getNoOfWheels())