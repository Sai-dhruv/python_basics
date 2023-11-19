class Test:
    count =0
    def __init__(self):
        Test.count += 1

    @classmethod
    def noofObjects(cls):
        print("No of objects",cls.count)

t1= Test()
t2= Test()
Test.noofObjects()            
