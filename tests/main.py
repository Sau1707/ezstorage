from classdb import key
from classdb.sqlite import sqlitedb, SqliteReader

@sqlitedb()
class Test:
    key: key.str
    number: int
    lista: list
    dizi: dict
    

test = SqliteReader(Test)

print(test)