def deco_1(func):
    def inner(name):
        print("Deco_1 called and name is ", name)
        func(name)
    return inner

def deco_2(func):
    def inner(name):
        print("Deco_2 called and name is ", name)
        func(name)
    return inner

@deco_1
@deco_2
def wish(name):
    print("Wish function calling and name is :", name)

wish("Saikrishna")    



