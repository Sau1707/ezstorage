'''
    Global reader, depending on the type of the class decorator
    instantiate the correct reader
'''
from .sqlite.reader import SqliteReader

class Reader:
    '''
        Useful to read and seach content of a table
    '''

    def __init__(self, cls) -> None:
        if not hasattr(cls, "_classdb_type"):
            raise ValueError("The passed class has to be decorated with a classdb decorator")
        if cls._classdb_type == "sqlite":
            self.reader = SqliteReader(cls)

        if not hasattr(self, "reader"):
            raise ValueError("The reader for this decorator type has not been implemented yet")

    def readAll(self):
        '''
            Read all the content of the given table, return array of class
        '''
        return self.reader.readAll()
    
    def find(self, **kwargs):
        '''
            Seach for match in the table, return array of class
        '''
        return self.reader.find(**kwargs)
    
