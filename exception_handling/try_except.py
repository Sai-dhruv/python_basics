VALUE = 200

def demo():
    print("I am printing before try block")
    try:
        print("I am pring first line in try block")
        a = 10/0
        print("A value is :",a)
        print("Printing value :", VALUE)
    except ZeroDivisionError:
        a = 10/2
        print("printing in the Exception block..a value ",a)
    

print("print the result :",demo())    



