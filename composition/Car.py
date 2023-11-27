class Car:
    def __init__(self,carName,model):
        self.carName= carName
        self.model=model
    
    def getCarInfo(self):
        print("car name : {} and model is {}".format(self.carName,self.model))

        

