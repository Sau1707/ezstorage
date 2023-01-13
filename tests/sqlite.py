from classdb import key
from classdb.sqlite import sqlitedb

@sqlitedb()
class TestStr:
    test_key: key.str
    test_number: int
    test_decimal: float
    test_string: str
    test_truth: bool
    test_array: list
    test_object: dict
    test_group: tuple

testStr = TestStr("test_key")
print(testStr)
testStr.test_number = 100
testStr.test_decimal = 10.1
testStr.test_string = "test"
testStr.test_truth = True
testStr.test_array = [1,2]
testStr.test_object = {"test": 1}
testStr.test_group= ("1", "2", "3")
print(testStr)
testStr.save()

testStr1 = TestStr("test_key")
print(testStr1)

