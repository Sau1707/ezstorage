# import libraries
import json, ast

# Import util
from ..costants import KEYS, SQLITE_KEYWORDS
from .util import getDefaultValue, createSchema
from .database import SQLite3

def sqlitedb(db="data.db"):
    def decorator(cls):
        def __init__(self, *args, **kwargs):
            # Inizialize the values with the default of each type, extract key
            key = None
            for field_name, field_type in self.__annotations__.items():
                if field_name.upper() in SQLITE_KEYWORDS:
                    raise ValueError(f"The key with name {field_name} is now allowed in a sqlite database")
                if field_type in KEYS:
                    if key: raise ValueError("Only one key type is allowed")
                    key = field_name
                if field_name in kwargs:
                    value = kwargs.get(field_name)
                    setattr(self, field_name, value)
                else:
                    setattr(self, field_name, getDefaultValue(field_type))
            if not key: raise ValueError("Key of the record missing")
            print(getattr(self, "indicator"))
            # Check and updathe the schema the first time the class is created
            if not hasattr(cls, "schema_attributes"):
                schema = createSchema(self.__annotations__)
                # Connect to the database
                cls.connector = SQLite3(db)
                # Inizialize the db, check if the schema are compatible
                cls.connector.setup(cls.__name__, schema)
                cls.schema_attributes = [field_name for field_name, _ in self.__annotations__.items()]
            # If a parameter is given, load from the database with that id
            if len(args) == 1:
                setattr(self, key, args[0])
                self.key_field_name = key
                self.load()
                pass # Load from database with that id
            else:
                self.key_field_name = key

        def __str__(self):
            values = {val: getattr(self, val) for val in self.schema_attributes}
            return json.dumps(values, indent=4)   

        def __repr__(self):
            # TODO: fix with pretty list and object
            values = ""
            for val in self.schema_attributes:
                values += f"{val}: {getattr(self, val)}, "
            values = values.rstrip(", ")
            return f"{cls.__name__}({values})"

        # Prevent overwrite of key field
        default_setter = cls.__setattr__
        def __setattr__(self, __name, __value):
            if (hasattr(self, "key_field_name") and __name == self.key_field_name):
                raise ValueError("You cannot modify the key of the field")
            default_setter(self, __name, __value)

        def save(self):
            values = {val: getattr(self, val) for val in self.schema_attributes}
            cls.connector.save(cls.__name__, self.key_field_name, values)

        def load(self):
            data = cls.connector.load(cls.__name__, self.key_field_name, getattr(self, self.key_field_name), self.schema_attributes)
            for key, value in data.items():
                if key == self.key_field_name: continue
                setattr(self, key, value) 

        cls.__init__ = __init__
        cls.__str__ = __str__
        cls.__repr__ = __repr__
        cls.__setattr__ = __setattr__
        cls.save = save
        cls.load = load
        cls.__filename__ = db

        return cls
    return decorator

