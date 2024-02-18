import unittest
from ezstorage.tokenizer import LambdaTokenizer, Token, TokenTypes
from ezstorage.table import Table


class Car(Table):
    id = 10
    number = 0


class TestTokenizer(unittest.TestCase):
    def test_tokenizer_with_equal(self):
        x = lambda: Car.id == 0
        tokens = LambdaTokenizer(x).tokenize()
        self.assertEqual(tokens, [Token("id", Car), Token("==", TokenTypes.EQUAL), Token("0", TokenTypes.CONSTANT)])

    def test_tokenizer_with_not_equal(self):
        x = lambda: Car.id != 0
        tokens = LambdaTokenizer(x).tokenize()
        self.assertEqual(tokens, [Token("id", Car), Token("!=", TokenTypes.NOT_EQUAL), Token("0", TokenTypes.CONSTANT)])

    def test_tokenizer_with_less_than(self):
        x = lambda: Car.id < 0
        tokens = LambdaTokenizer(x).tokenize()
        self.assertEqual(tokens, [Token("id", Car), Token("<", TokenTypes.LESS_THAN), Token("0", TokenTypes.CONSTANT)])

    def test_tokenizer_with_greater_than(self):
        x = lambda: Car.id > 0
        tokens = LambdaTokenizer(x).tokenize()
        self.assertEqual(tokens, [Token("id", Car), Token(">", TokenTypes.GREATER_THAN), Token("0", TokenTypes.CONSTANT)])

    def test_tokenizer_with_less_than_equal(self):
        x = lambda: Car.id <= 0
        tokens = LambdaTokenizer(x).tokenize()
        self.assertEqual(tokens, [Token("id", Car), Token("<=", TokenTypes.LESS_THAN_EQUAL), Token("0", TokenTypes.CONSTANT)])

    def test_tokenizer_with_greater_than_equal(self):
        x = lambda: Car.id >= 0
        tokens = LambdaTokenizer(x).tokenize()
        self.assertEqual(tokens, [Token("id", Car), Token(">=", TokenTypes.GREATER_THAN_EQUAL), Token("0", TokenTypes.CONSTANT)])

    def test_tokenizer_with_and(self):
        x = lambda: Car.id > 0 and Car.id < 10
        tokens = LambdaTokenizer(x).tokenize()
        self.assertEqual(tokens, [Token("id", Car), Token(">", TokenTypes.GREATER_THAN), Token("0", TokenTypes.CONSTANT), Token("and", TokenTypes.AND), Token("id", Car), Token("<", TokenTypes.LESS_THAN), Token("10", TokenTypes.CONSTANT)])

    def test_tokenizer_with_or(self):
        x = lambda: Car.id > 0 or Car.id < 10
        tokens = LambdaTokenizer(x).tokenize()
        self.assertEqual(tokens, [Token("id", Car), Token(">", TokenTypes.GREATER_THAN), Token("0", TokenTypes.CONSTANT), Token("or", TokenTypes.OR), Token("id", Car), Token("<", TokenTypes.LESS_THAN), Token("10", TokenTypes.CONSTANT)])

    def test_tokenizer_with_parentheses(self):
        x = lambda: (Car.id > 0 and Car.id < 10) or Car.id == 0
        tokens = LambdaTokenizer(x).tokenize()
        self.assertEqual(tokens, [Token("(", TokenTypes.OPEN_PARENTHESIS), Token("id", Car), Token(">", TokenTypes.GREATER_THAN), Token("0", TokenTypes.CONSTANT), Token("and", TokenTypes.AND), Token("id", Car), Token("<", TokenTypes.LESS_THAN), Token("10", TokenTypes.CONSTANT), Token(")", TokenTypes.CLOSE_PARENTHESIS), Token("or", TokenTypes.OR), Token("id", Car), Token("==", TokenTypes.EQUAL), Token("0", TokenTypes.CONSTANT)])

    def test_tokenizer_with_nested_parentheses(self):
        x = lambda: (Car.id > 0 and Car.id < 10) or (Car.id == 0 and Car.id != 0)
        tokens = LambdaTokenizer(x).tokenize()
        self.assertEqual(tokens, [Token("(", TokenTypes.OPEN_PARENTHESIS), Token("id", Car), Token(">", TokenTypes.GREATER_THAN), Token("0", TokenTypes.CONSTANT), Token("and", TokenTypes.AND), Token("id", Car), Token("<", TokenTypes.LESS_THAN), Token("10", TokenTypes.CONSTANT), Token(")", TokenTypes.CLOSE_PARENTHESIS), Token("or", TokenTypes.OR), Token("(", TokenTypes.OPEN_PARENTHESIS), Token("id", Car), Token("==", TokenTypes.EQUAL), Token("0", TokenTypes.CONSTANT), Token("and", TokenTypes.AND), Token("id", Car), Token("!=", TokenTypes.NOT_EQUAL), Token("0", TokenTypes.CONSTANT), Token(")", TokenTypes.CLOSE_PARENTHESIS)])

    def test_tokenizer_with_variable(self):
        var = 0
        x = lambda: Car.id > var
        tokens = LambdaTokenizer(x).tokenize()
        self.assertEqual(tokens, [Token("id", Car), Token(">", TokenTypes.GREATER_THAN), Token("0", TokenTypes.CONSTANT)])

    def test_tokenizer_inline_declaration(self):
        tokens = LambdaTokenizer(lambda: Car.id > 0).tokenize()
        self.assertEqual(tokens, [Token("id", Car), Token(">", TokenTypes.GREATER_THAN), Token("0", TokenTypes.CONSTANT)])

if __name__ == '__main__':
    unittest.main()