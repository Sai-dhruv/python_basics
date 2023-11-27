class Book:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        return self.pages+other.pages
    
    def __gt__(self,other):
        return self.pages>other.pages

    def __lt__(self,other):
        return self.pages<other.pages



b1 = Book(100)
b2 = Book(200)
print("Adding two books :", b1+b2)
print("Adding two books :", b1<b2)
print("Adding two books :", b1>b2)
