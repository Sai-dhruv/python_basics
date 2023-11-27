class Test:
    count = 0
    def __init__(self):
        Test.count += 1

    def noOfObjectsCreated(): # static method
        print("No of objects :",Test.count)

t1 = Test()
t2 = Test()
t3 = Test()
Test.noOfObjectsCreated()
