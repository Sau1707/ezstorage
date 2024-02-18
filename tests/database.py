import os
import unittest
from ezstorage import Table, Sqlite


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Sqlite("test.db")

    def tearDown(self):
        self.db.close()
        del self.db
        os.remove("test.db")

    def test_table_creation(self):
        """Test that the table is created in the database when the create_table method is called."""
        @self.db.useTable("test_table")
        class TestTable(Table):
            id: int
            name: str
            age: int

        self.db.create_table(TestTable)
        schema = self.db._get_schema(TestTable)
        self.assertEqual(schema, {"id": "INTEGER", "name": "TEXT", "age": "INTEGER"})
    
    def test_table_deletion(self):
        """Test that the table is deleted from the database when the drop_table method is called."""
        @self.db.useTable("test_table")
        class TestTable(Table):
            id: int
            name: str
            age: int

        self.db.create_table(TestTable)
        self.db.drop_table(TestTable)
        self.assertEqual(self.db._get_schema(TestTable), {})


    def test_table_column_creation(self):
        """Test that the table is updated in the database when the update_table method is called."""
        @self.db.useTable("test_table")
        class TestTable(Table):
            id: int
            name: str

        self.db.create_table(TestTable)

        @self.db.useTable("test_table")
        class TestTable(Table):
            id: int
            name: str
            age: int

        self.db.update_table(TestTable)
        schema = self.db._get_schema(TestTable)
        self.assertEqual(schema, {"id": "INTEGER", "name": "TEXT", "age": "INTEGER"})

    def test_table_column_deletion(self):
        """Test that the table is updated in the database when the update_table method is called."""
        @self.db.useTable("test_table")
        class TestTable(Table):
            id: int
            name: str
            age: int

        self.db.create_table(TestTable)

        @self.db.useTable("test_table")
        class TestTable(Table):
            id: int
            name: str

        self.db.update_table(TestTable)
        schema = self.db._get_schema(TestTable)
        self.assertEqual(schema, {"id": "INTEGER", "name": "TEXT"})

    def test_table_column_update(self):
        """Test that the table is updated in the database when the update_table method is called."""
        @self.db.useTable("test_table")
        class TestTable(Table):
            id: int
            name: str
            age: int

        self.db.create_table(TestTable)

        with self.assertRaises(AssertionError):
            @self.db.useTable("test_table")
            class TestTable(Table):
                id: int
                name: str
                age: str


if __name__ == "__main__":
    unittest.main()
