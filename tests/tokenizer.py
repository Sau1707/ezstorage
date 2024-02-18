import unittest
from ezstorage.tokenizer import LambdaTokenizer

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
    pass

def create_test_function(test_string, expected):
    def test(self):
        tokens = LambdaTokenizer(test_string).tokenize()
        self.assertEqual(tokens, expected)
    return test

# Dynamically add test methods to the TestTokenizerDynamicallyGenerated class
for test_name, (test_string, expected) in enumerate(tokenizer_tests_string.items()):
    test_method_name = f'test_{test_name:04d}_{test_string[:10].replace(" ", "_").replace(".", "_")}'
    test_method = create_test_function(test_string, expected)
    setattr(TestTokenizerDynamicallyGenerated, test_method_name, test_method)


class TestLambdaCleanTokenizer(unittest.TestCase):
    def test_lambda_tokenizer_with_variable(self):
        x = lambda: Car.id > 0
        cleaned = LambdaTokenizer.clean_lambda(x)
        self.assertEqual(cleaned, "Car.id > 0")

    def test_lambda_tokenizer_with_long_variable(self):
        x = lambda: Car.id < 0 and Car.id > 0 and Car.id == 0 or Car.id != 0
        cleaned = LambdaTokenizer.clean_lambda(x)
        self.assertEqual(cleaned, "Car.id < 0 and Car.id > 0 and Car.id == 0 or Car.id != 0")

    def test_lambda_tokenizer_with_long_variable_and_parentheses(self):
        x = lambda: (Car.id < 0 and Car.id > 0) and Car.id == 0 or Car.id != 0
        cleaned = LambdaTokenizer.clean_lambda(x)
        self.assertEqual(cleaned, "(Car.id < 0 and Car.id > 0) and Car.id == 0 or Car.id != 0")

    def test_lambda_tokenizer_with_long_variable_and_parentheses_and_nested_parentheses(self):
        x = lambda: (Car.id < 0 and Car.id > 0) and (Car.id == 0 or Car.id != 0)
        cleaned = LambdaTokenizer.clean_lambda(x)
        self.assertEqual(cleaned, "(Car.id < 0 and Car.id > 0) and (Car.id == 0 or Car.id != 0)")

    def test_lambda_tokenizer_with_long_variable_and_parentheses_and_nested_parentheses_and_nested_parentheses(self):
        x = lambda: (Car.id < 0 and Car.id > 0) and (Car.id == 0 or (Car.id != 0 and Car.id >= 0))
        cleaned = LambdaTokenizer.clean_lambda(x)
        self.assertEqual(cleaned, "(Car.id < 0 and Car.id > 0) and (Car.id == 0 or (Car.id != 0 and Car.id >= 0))")

    def test_lambda_tokenizer_with_variable(self):
        var = 0
        x = lambda: Car.id > var
        cleaned = LambdaTokenizer.clean_lambda(x)
        self.assertEqual(cleaned, "Car.id > var")

    def test_lambda_tokenizer_inline_declaration(self):
        cleaned = LambdaTokenizer.clean_lambda(lambda: Car.id > 0)
        self.assertEqual(cleaned, "Car.id > 0")

    def test_lambda_tokenizer_inline_declaration_with_nested_parentheses(self):
        cleaned = LambdaTokenizer.clean_lambda(lambda: (Car.id < 0 and Car.id > 0) and (Car.id == 0 or (Car.id != 0 and Car.id >= 0)))
        self.assertEqual(cleaned, "(Car.id < 0 and Car.id > 0) and (Car.id == 0 or (Car.id != 0 and Car.id >= 0))")

    def test_lambda_tokenizer_in_object(self):
        obj = {
            "x": lambda: Car.id > 0
        }
        cleaned = LambdaTokenizer.clean_lambda(obj["x"])
        self.assertEqual(cleaned, "Car.id > 0")

#############################################################################
#
#############################################################################
if __name__ == '__main__':
    unittest.main()