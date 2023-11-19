class TooYoungException(Exception):
    def __init__(self,args):
        self.msg = args

a = int(input("Enter the age"))
if(a > 60):
    raise TooYoungException("Custom defind exception working .. Message printing.. Cool")
else:
    print("Great..")        

    