def decor1(func):
    def inner(name):
        print("Step 2 : Decor 1 is executing , for decor 1 Wish function is Input ")
        func(name)
        print("Step 4 : Decor 1  is input to decor 2")    
    return inner
def decor2(func):
    def inner(name):
        print("Step 1 : Now in docor 2 ,  will execute coz this is top one - For this Docor 1 is the input , In next line calling fun")
        func(name)
        print("Step 5 : Came here After executing decor 1 function - Final step ")
    return inner    

@decor2
@decor1
def wish(name):
    print("Step 3 this will input to decor 1 : Good morning ", name)

wish("Saikrishna ")    