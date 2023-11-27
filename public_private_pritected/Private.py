class PrivateExample:
    def __init__(self):
        self.__x = 10 # This is private variable __

e = PrivateExample()
#print(e.__x)        
# To access private varibale 
print(e._PrivateExample__x) # ObjectReference._classname__variablename

