def wish(name):
    print("Good Morning ",name)

greet = wish
print(id(wish))
print(id(greet))
wish("saikrishna")
greet("Vinjamuri")    