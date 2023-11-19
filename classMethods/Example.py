class Animal:
    legs = 4
    @classmethod
    def walk(cls,name):
        print("{} Walk with {} legs".format(name,cls.legs))

Animal.walk("Dog")    

a = Animal()
a.walk("Cat")
