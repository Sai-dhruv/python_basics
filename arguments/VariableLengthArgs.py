def sum(*n):
    print("This will take in the form of tuple")
    result = 0
    for i in n:
        result = result +i
        print("Result :",result)

sum(10)        
sum(10,20)