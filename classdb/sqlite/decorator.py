# import libraries
import json, sqlite3, ast

# Import util
from ..costants import KEYS, SQLITE_KEYWORDS
from .util import getDefaultValue, createSchema
from .database import setup, load, save

def sqlitedb(db="data.db"):
    def decorator(cls):
        class Wrapper(cls):
            def __init__(self, *args, **kwargs):
                # Inizialize the values with the default of each type
                schema_attributes = []
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
                    schema_attributes.append(field_name)
                if not key: raise ValueError("Key of the record missing")
                self.schema_attributes = schema_attributes
                
                # Check and updathe the schema the first time the class is created
                if not hasattr(cls, "instance_created"):
                    cls.instance_created = False
                    schema = createSchema(self.__annotations__)
                    # Connect to the database
                    cls.connector = sqlite3.connect(db)
                    cls.table_name = cls.__class__.__name__
                    # Inizialize the db, check if the schema are compatible
                    setup(cls.connector, cls.table_name, schema)
                self.connector = cls.connector
                self.table_name = cls.table_name

                # check if a paremeter is given
                if len(args) == 1:
                    setattr(self, key, args[0])
                    self.key_field_name = key
                    self.load()
                    pass # Load from database with that id
                else:
                    self.key_field_name = key

                if (cls.__init__ != object.__init__):
                    super().__init__(*args, **kwargs)

            # Convert object to string
            def __str__(self):
                if (cls.__str__ != object.__str__):
                    return super().__str__(self)
                values = {val: getattr(self, val) for val in self.schema_attributes}
                return json.dumps(values, indent=4)

            # Prevent overwrite of key field
            def __setattr__(self, __name, __value):
                if (hasattr(self, "key_field_name") and __name == self.key_field_name):
                    raise ValueError("You cannot modify the key of the field")
                return super().__setattr__(__name, __value)

            # Save value into the db
            def save(self):
                values = {val: getattr(self, val) for val in self.schema_attributes}
                save(self.connector, self.table_name, self.key_field_name, values)

            # Load the values given the key
            def load(self):
                data = load(self.connector, self.table_name, self.key_field_name, getattr(self, self.key_field_name), self.schema_attributes)
                for key, value in data.items():
                    if key == self.key_field_name: 
                        continue
                    if isinstance(value, (int, float)):
                        setattr(self, key, value) 
                    else:   
                        try:
                            setattr(self, key, ast.literal_eval(value))   
                        except:
                            setattr(self, key, value)   

        Wrapper.__name__ = cls.__name__
        Wrapper.__annotations__ = cls.__annotations__
        return Wrapper
    return decorator

