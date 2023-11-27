class Person:
    def __init__(self):
        self.name = 'Durga'
        self.db = self.dob()

    def display(self):
        print("Name :",self.name)

    class dob:
        def __init__(self):
            print(' The dob is {}/{}/{}'.format('05','14','1990'))        


p= Person()        