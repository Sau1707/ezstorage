import unittest
from ezstorage import Table, Sqlite


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.db = Sqlite('test.db')

    def test_create_instance_with_missing_decorator(self):
        """Test if the table is created without the decorator"""
        class User(Table):
            name: str
            age: int

        with self.assertRaises(AssertionError):
            User(name='John', age=25)

    def test_create_instance_with_wrong_key(self):
        """Test if the table is created with a wrong key"""
        @self.db.useTable("table_name")
        class User(Table):
            id: int
            name: str
        
        with self.assertRaises(AssertionError):
            User(name='John', wrong_key='test')

    def test_create_instance_with_missing_key(self):
        """Test if the table is created with a missing key"""
        @self.db.useTable("table_name")
        class User(Table):
            id: int
            name: str
        
        with self.assertRaises(AssertionError):
            User(name='John')

    def test_valid_instance(self):
        """Test if the table is created with the correct keys"""
        @self.db.useTable("table_name")
        class User(Table):
            id: int
            name: str

        user = User(id=1, name='John')
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, 'John')

if __name__ == '__main__':
    unittest.main()