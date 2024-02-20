import unittest
import ezstorage as ez


class TestTypes(unittest.TestCase):
    def setUp(self) -> None:
        self.db = ez.Sqlite(":memory:")

    def tearDown(self) -> None:
        self.db.drop_tables()
        self.db.close()
        self.db = None

    def test_type_int(self):
        @self.db.useTable("test_table")
        class Test(ez.Table):
            key: int

        self.db.create_tables()
        with self.db:
            Test(key=0)
        
        content = Test.where()
        self.assertEqual(content, [Test(key=0)])


if __name__ == "__main__":
    unittest.main()