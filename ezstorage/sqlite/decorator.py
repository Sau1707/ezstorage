# Import util
from ..costants import KEYS, SQLITE_KEYWORDS
from .util import getDefaultValue, createSchema
from .database import SQLite3

def sqlite(db="data.db"):
    def decorator(cls):
        def __init__(self, *args, **kwargs):
            # Inizialize the values with the default of each type, extract key
            key = None
            for field_name, field_type in self.__annotations__.items():
                if field_name.upper() in SQLITE_KEYWORDS:
                    raise ValueError(f"The key with name {field_name} is now allowed in a sqlite database")
                if field_type in KEYS:
                    if key: 
                        raise ValueError("Only one key type is allowed")
                    key = field_name
                if field_name in kwargs:
                    setattr(self, field_name, kwargs.get(field_name))
                else:
                    setattr(self, field_name, getDefaultValue(field_type))
            if not key: 
                raise ValueError("Key of the record missing")

            # Check and update the schema the first time the class is created
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
            else:
                self.key_field_name = key

        def __str__(self):
            return self.__repr__()
            # values = {val: getattr(self, val) for val in self.schema_attributes}
            # return json.dumps(values, indent=4)   

        def __repr__(self):
            # TODO: fix with pretty list and object
            values = ""
            for val in self.schema_attributes:
                values += f"{val}: {getattr(self, val)}, "
            values = values.rstrip(", ")
            return f"{cls.__name__}({values})"

        def __dict__(self):
            obj = {}
            for val in self.schema_attributes:
                obj[val] = getattr(self, val)
            return obj

        # Prevent overwrite of key field
        default_setter = cls.__setattr__
        def __setattr__(self, __name, __value):
            if (hasattr(self, "key_field_name") and __name == self.key_field_name):
                raise ValueError("You cannot modify the key of the field")
            if __name != "_match_db":
                self._match_db = False
            default_setter(self, __name, __value)

        def __getitem__(self, item):
            return getattr(self, item)

        def save(self):
            '''
                Save the current class state to the database
            '''
            values = {val: getattr(self, val) for val in self.schema_attributes}
            cls.connector.save(cls.__name__, self.key_field_name, values)
            self._match_db = True

        def load(self):
            '''
                Load the content of the database entry to the class
            '''
            data = cls.connector.load(cls.__name__, self.key_field_name, getattr(self, self.key_field_name), self.schema_attributes)
            for key, value in data.items():
                if key == self.key_field_name: continue
                setattr(self, key, value) 
            self._match_db = bool(data)
            
        def remove(self):
            '''
                Remove the current class from the database, with the key
            '''
            cls.connector.remove(cls.__name__, self.key_field_name, getattr(self, self.key_field_name))
            self._match_db = False

        def match(self):
            '''
                Return true if the state of the class match the entry of the database
            '''
            return self._match_db

        cls.__init__ = __init__
        cls.__str__ = __str__
        cls.__repr__ = __repr__
        cls.__setattr__ = __setattr__
        cls.__getitem__ = __getitem__
        cls.save = save
        cls.load = load
        cls.remove = remove
        cls.match = match
        cls.__filename__ = db
        cls._classdb_type = "sqlite"

        return cls
    return decorator

