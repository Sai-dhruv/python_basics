class GF:
    def land(self):
        print("Land from GF")

class F(GF):
    def cash(self):
        print("Cash from Father")

class Person(F):
    def business(self):
        print("Doing Business")


p = Person()
p.land()
p.cash()
p.business()