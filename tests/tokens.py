import unittest
from ezstorage.tokenizer import LambdaTokenizer, Token

# Define some classes to use in the tests
def get_number():
    return 0

class Car:
    id = 0
    number = 0

class Mouse:
    id = 0

class Cat:
    number = 0

this_is = 0
thisIs = 0

tokenizer_tests_string = {
    "Car.id > 0": ["Car.id", ">", "0"],
    "Car.id < 0": ["Car.id", "<", "0"],
    "Car.id == 0": ["Car.id", "==", "0"],
    "Car.id == number": ["Car.id", "==", "number"],
    "Car.id != 0": ["Car.id", "!=", "0"],
    "Car.id >= 0": ["Car.id", ">=", "0"],
    "Car.id <= 0": ["Car.id", "<=", "0"],
    "Car.id in []": ["Car.id", "in", "[]"],
    "Car.id not in []": ["Car.id", "not in", "[]"],
    "Car.id in array": ["Car.id", "in", "array"],
    "(Car.id and Car.id) or Car.id": ["(", "Car.id", "and", "Car.id", ")", "or", "Car.id"],
    "(Car.id or Car.id) and Car.id": ["(", "Car.id", "or", "Car.id", ")", "and", "Car.id"],
    "(Car.id and Car.id) and Car.id": ["(", "Car.id", "and", "Car.id", ")", "and", "Car.id"],
    "(Car.id or Car.id) or Car.id": ["(", "Car.id", "or", "Car.id", ")", "or", "Car.id"],
    "Car.id>0": ["Car.id", ">", "0"],
    "Car.id<0": ["Car.id", "<", "0"],
    "Car.id==0": ["Car.id", "==", "0"],
    "Car.id==number": ["Car.id", "==", "number"],
    "Car.id==\"number\"": ["Car.id", "==", "\"number\""],
    "Car.id!=0": ["Car.id", "!=", "0"],
    "Car.id>=0": ["Car.id", ">=", "0"],
    "Car.id<=0": ["Car.id", "<=", "0"],
    "Car.id in[]": ["Car.id", "in", "[]"],
    "Car.id not in[]": ["Car.id", "not in", "[]"],
    "Car.id in array": ["Car.id", "in", "array"],
    "(Car.id and Car.id)or Car.id": ["(", "Car.id", "and", "Car.id", ")", "or", "Car.id"],
    "(Car.id or Car.id)and Car.id": ["(", "Car.id", "or", "Car.id", ")", "and", "Car.id"],
    "(Car.id and Car.id)and Car.id": ["(", "Car.id", "and", "Car.id", ")", "and", "Car.id"],
    "(Car.id or Car.id)or Car.id": ["(", "Car.id", "or", "Car.id", ")", "or", "Car.id"],
    "Car.id > get_number()": ["Car.id", ">", "get_number()"],
    "Car.id < get_number()": ["Car.id", "<", "get_number()"],
    "Car.id == get_number()": ["Car.id", "==", "get_number()"],
    "Car.id != get_number()": ["Car.id", "!=", "get_number()"],
    "0 < Car.id": ["0", "<", "Car.id"],
    "0 > Car.id": ["0", ">", "Car.id"],
    "0 == Car.id": ["0", "==", "Car.id"],
    "0 != Car.id": ["0", "!=", "Car.id"],
    "0 <= Car.id": ["0", "<=", "Car.id"],
    "0 >= Car.id": ["0", ">=", "Car.id"],
    "[] in Car.id": ["[]", "in", "Car.id"],
    "Car.id > Car.number": ["Car.id", ">", "Car.number"],
    "Car.id < Car.number": ["Car.id", "<", "Car.number"],
    "Mouse.id == Cat.number": ["Mouse.id", "==", "Cat.number"],
    "Mouse.id != Cat.number": ["Mouse.id", "!=", "Cat.number"],
    "Mouse.id >= this_is": ["Mouse.id", ">=", "this_is"],
    "Mouse.id <= thisIs": ["Mouse.id", "<=", "thisIs"],
}


# Test the function with the provided example strings
class TestTokenizerDynamicallyGenerated(unittest.TestCase):
    """Test the lambda expression tokenizer with dynamically generated tests"""
    pass

def create_test_function(test_string, expected):
    def test(self):
        tokens = LambdaTokenizer(test_string).get_tokens()
        self.assertEqual(tokens, expected)
    return test

# Dynamically add test methods to the TestTokenizerDynamicallyGenerated class
for test_name, (test_string, expected) in enumerate(tokenizer_tests_string.items()):
    test_method_name = f'test_{test_name:04d}_{test_string[:10].replace(" ", "_").replace(".", "_")}'
    test_method = create_test_function(test_string, expected)
    setattr(TestTokenizerDynamicallyGenerated, test_method_name, test_method)


if __name__ == "__main__":
    unittest.main()