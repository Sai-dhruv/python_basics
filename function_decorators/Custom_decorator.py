def double_decor(fun):
    def inner():
        x = fun()
        return 2*x
    return inner

def square_decor(fun):
    def inner():
        x = fun()
        return x*x
    return inner

@double_decor # for this Square Decor is input
@square_decor # FOr this num is the input
def num():
    return 10

#double_decor(square_decor(num))
print(num())