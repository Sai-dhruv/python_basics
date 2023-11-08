def singleExcept():
    try:
        a = int(input("Enter 1st Number  :"))
        b = int(input("Enter 2nd Number  :"))
        x = a / b
        print("X values is ",x)
    except (ZeroDivisionError, ValueError)as msg:
        print("Exception Message is ",msg)

    except:
        print("Default except except Block shold be last")    

singleExcept()


