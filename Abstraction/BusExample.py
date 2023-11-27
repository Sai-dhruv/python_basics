from abc import *

class Vehicle(ABC):
    @abstractmethod
    def getNoofWheels(self):
        pass

class Bus(Vehicle):
    def getNoofWheels(self):
        return 7

b = Bus()
print(b.getNoofWheels())