from functools import reduce

l =[10,20,30]
result = reduce(lambda x,y:x+y,l)
print("FInal value :",result)

print(sum([1,2,3,4]))