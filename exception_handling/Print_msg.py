def print_exception_msg():
    try:
        10/0
    except ZeroDivisionError as msg:
        print("Exception message is :",msg)

print_exception_msg()            