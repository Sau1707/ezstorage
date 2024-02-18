import os
import unittest
from ezstorage import Table, Sqlite


class TestMagicMethods(unittest.TestCase):
    def setUp(self):
        self.db = Sqlite('test.db')

    def tearDown(self) -> None:
        self.db.close()
        self.db = None
        os.remove('test.db')

    def test_repr(self):
        """Test the __repr__ method"""
        @self.db.useTable("table_name")
        class User(Table):
            id: int
            name: str
        
        user = User(id=1, name='John')
        self.assertEqual(repr(user), "User(id=1, name=John)")

    def test_iter(self):
        """Test the __iter__ method"""
        @self.db.useTable("table_name")
        class User(Table):
            id: int
            name: str
        
        user = User(id=1, name='John')
        self.assertEqual(list(user), [('id', 1), ('name', 'John')])

    def test_getitem(self):
        """Test the __getitem__ method"""
        @self.db.useTable("table_name")
        class User(Table):
            id: int
            name: str
        
        user = User(id=1, name='John')
        self.assertEqual(user['id'], 1)
        self.assertEqual(user['name'], 'John')
    
    def test_setitem(self):
        """Test the __setitem__ method"""
        @self.db.useTable("table_name")
        class User(Table):
            id: int
            name: str
        
        user = User(id=1, name='John')
        user['id'] = 2
        user['name'] = 'Jane'
        self.assertEqual(user['id'], 2)
        self.assertEqual(user['name'], 'Jane')

    def test_len(self):
        """Test the __len__ method"""
        @self.db.useTable("table_name")
        class User(Table):
            id: int
            name: str
        
        user = User(id=1, name='John')
        self.assertEqual(len(user), 2)

    def test_contains(self):
        """Test the __contains__ method"""
        @self.db.useTable("table_name")
        class User(Table):
            id: int
            name: str
        
        user = User(id=1, name='John')
        self.assertTrue('id' in user)
        self.assertFalse('age' in user)

    def test_eq(self):
        """Test the __eq__ method"""
        @self.db.useTable("table_name")
        class User(Table):
            id: int
            name: str
        
        user1 = User(id=1, name='John')
        user2 = User(id=1, name='John')
        self.assertEqual(user1, user2)
        self.assertNotEqual(user1, User(id=2, name='Jane'))


if __name__ == '__main__':
    unittest.main()