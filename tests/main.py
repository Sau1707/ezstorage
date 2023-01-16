from ezstorage import key
from ezstorage.sqlite import sqlitedb, SqliteReader

@sqlitedb()
class Test:
    indicator: key.str
    number: int
    lista: list
    dizi: dict
    
t = Test(indicator="test", number=10, lista=[1,2,3], dizi={"d": "demo"})
print(t.indicator)
t.number = 20
t.save()

t1 = Test(indicator="test1", number=10, lista=[1,2,3], dizi={"d": "demo"})
print(t1)
t1.save()

t2 = Test("test1")
print(t2)
#test = SqliteReader(Test)
#test.readAll()

reader = SqliteReader(Test)
all = reader.readAll()
fil = reader.find(lista=[1,2,3])
print(fil)
