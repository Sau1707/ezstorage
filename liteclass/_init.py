'''
    Overwrite the init of the class
'''
# The init take as parametr the database name
import sqlite3
from .constants import DEAFAULT_VALUES
from .database import createSchema, setup

def getDefaultValue(field_type):
    """
    Return the default value for a given type
    """
    default_value = DEAFAULT_VALUES.get(field_type)
    if default_value is None: 
        raise ValueError(f"Unsupported field type {field_type}")
    return default_value

def _Init(cls, db):
    """
    Modify the class's __init__ method to initialize fields with default values.
    """
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        # If a single value is passed, then grab the data from the database with that key
        # If a lot of value are parred, create a new entry in the database
        print(args)
        print(kwargs)

        # Inizialize the values with the default of each type
        schema_attributes = []
        for field_name, field_type in self.__annotations__.items(): 
            if field_name in kwargs:
                value = kwargs.get(field_name)
                if not isinstance(value, field_type):
                    raise ValueError(f"{field_name} should be of type {field_type}")
                setattr(self, field_name, value)
            else:
                setattr(self, field_name, getDefaultValue(field_type))
            schema_attributes.append(field_name)
        self.schema_attributes = schema_attributes

        # Create the schema
        schema = createSchema(self.__annotations__)

        # Connect to the database
        self.conn = sqlite3.connect(db)
        self.table = cls.__class__.__name__

        # Inizialize the db, check if the schema are compatible
        setup(self.conn, self.table, schema)

        original_init(self)

    cls.__init__ = new_init