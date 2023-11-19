def nested():
    try:
        print("Outer Except Block")
        try:
            print("Inner Except Block")
            a = 10/0
            print("After Exception")
        except ZeroDivisionError as msg:
            print("Inner Except Message :", msg)
        finally:
            print("FInally Executted Inner")

    except BaseException as b:
        print("Exception message :",b)

    finally:
        print("Finally Executted in Outer...")   


nested()         
