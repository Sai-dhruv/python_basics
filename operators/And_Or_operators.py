def example():
    list = [1,2,3,4,5,6,"sai","niha","Dhruv"]
    for i in list:
        if i == 3:
            continue
        if i == "sai" and "Dhruv" in list and "niha" in list:
            print(i ," is a Great person")
        if i == "niha" or i == "sai":
            print(i, "is a Proud parent of Dhruv")

example()            
           

