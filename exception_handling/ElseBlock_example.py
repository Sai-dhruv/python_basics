def elseExample():
    try:
        a = 10/2
        print("There is no excepton so a value =",a)
    except ZeroDivisionError as msg:
        print("Id Exception occur then then this try block will execure , It should match with except ")
    else:
        print("If there is no exception then else block will execute ")
    finally:
        print("Finally will execute irrespective of exception , This should execute always")


elseExample()