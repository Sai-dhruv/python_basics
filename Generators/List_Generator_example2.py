def countDown(num):
    print("STart count down ")
    while(num > 0):
        yield num
        num = num -1

values = countDown(5)
print("These are not values this type is :", type(values))
print("Data :", values)  # this is Generator object
for x in values:
    print(x)  

l = [x for x in range(5)] # Data will be stored in memory here 
for i in l:
    print(i)    


