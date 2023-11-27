class Outer:
    def m1(self):
        print("Outer class method called...")
    class Inner:
            def m2(self):
                print("Inner method called..")

o = Outer()
o.m1()   
i = o.Inner()
i.m2()    

Outer().Inner().m2()