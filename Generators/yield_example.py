def generator():
    yield 'A'
    yield 'B'
    yield 'C'

value = generator()
#print(type(value))
#print(next(value))
#print(next(value))
#print(next(value))
print("-------------------Generate one by one -----memory and performance i svery goo---------------------")

for i in value:
    print(i)

