from liteclass import Tableclass, PrimaryKey

@Tableclass()
class Test:
    i: PrimaryKey.int
    f: float
    s: str
    b: bool
    t: tuple
    l: list
    d: dict
    


test = Test()
print(test)
