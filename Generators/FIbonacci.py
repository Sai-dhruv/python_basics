def fib():
    a , b = 0,1
    while True:
        yield a
        a , b = b, a+b

f = fib()
for x in f:
    if x > 100:
        break
    print(x)        
