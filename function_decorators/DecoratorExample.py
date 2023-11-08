def decor(fun):
    def inner(name):
        if name == "Saikrishna":
            print("Hello Saikrishna Good evening")
        else:
            fun(name)    
    return inner       

@decor
def wish(name):
    print("Hello ", name ,"Good morning")

wish("saisarath")
wish("Saikrishna")    