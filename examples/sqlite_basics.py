from classdb import key
from classdb.sqlite import sqlitedb, SqliteReader

@sqlitedb()
class Demo:
    name: key.str
    number: int

data = Demo(name="example", number= 100)
print(data) # Demo(name: example, number: 100)
data.save()

data = Demo("example")
print(data) # Demo(name: example, number: 100)

