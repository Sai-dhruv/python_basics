from random import randint

for i in range(10):
    print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9), sep=' ')
    #print(str(randint(0,9))*5,sep=' ')  # This logic will not work 
    #print(randint(00000,99999), sep=' ') # this also