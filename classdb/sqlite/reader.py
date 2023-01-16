'''
    General reader function
'''
from .database import SQLite3

class SqliteReader:
    def __init__(self, cls) -> None:
        self.table_name = cls.__name__
        self.filename = cls.__filename__  
        self.cls = cls
        self.connector = SQLite3(self.filename)
        
    def readAll(self):
        '''
            Read the content of the database table and return the data
        '''
        data = self.connector.readTable(self.table_name)
        return [self.cls(**d) for d in data]

    def read(self, count):
        '''
            Read the given count of elements
        '''
        # TODO
        pass

    def find(self, **kwargs):
        '''
            Seach in database for the keyword, return array of data
        '''
        data = self.connector.find(self.table_name, **kwargs)
        return [self.cls(**d) for d in data]