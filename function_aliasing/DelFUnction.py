def wish(name):
    print("Good Morning ",name)

greet = wish
del wish

print(id(greet))

greet("Vinjamuri") 