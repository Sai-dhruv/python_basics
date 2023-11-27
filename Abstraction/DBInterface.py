from abc import *

class DBInterface:
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class Oracle(DBInterface):
    def connect(self):
        print('Coonecting oracle BD')

    def disconnect(self):
        print('disconnecting')

class mysql(DBInterface):
    def connect(self):
        print('connect to mysql')

    def disconnect(self):
        print('disconnecting mysql..')


dbName = input("Enter the DB name ")
className = globals()[dbName]
x=className()
x.connect()
x.disconnect()



