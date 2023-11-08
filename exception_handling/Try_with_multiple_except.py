def tryWithMultipleExcept():
    try:
        a = int(input("Enter first Number : "))
        b = int(input("Enter second Number : "))
        x = a / b
        print("x Value is :",x)
    except ZeroDivisionError as msg_1:
        print("message :",msg_1)
    except ValueError as msg_2:
        print("Message is :", msg_2)    


tryWithMultipleExcept()