from liteclass import Tableclass

@Tableclass
class Test:
    a: str



test = Test()
print(test.a)
