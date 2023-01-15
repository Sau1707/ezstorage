from classdb import key
from classdb.sqlite import sqlitedb, SqliteReader

@sqlitedb()
class Demo:
    name: key.str
    number: int

data = Demo(name="john", number= 1)
data.save()
data.number = 10
print(data) # Demo(name: john, number: 10)
data.load()
print(data) # Demo(name: john, number: 1)

