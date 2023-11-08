def decor(fun):
    def inner(name):
        if name == "Saikrishna":
            print("Hello Saikrishna Good evening")
        else:
            fun(name)    
    return inner       
def wish(name):
    print("Hello ", name ,"Good morning")

decorFunction = decor(wish) # Calling Explicitly

wish("saisarath")
decorFunction("Saikrishna")    