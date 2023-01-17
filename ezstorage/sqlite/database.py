import sqlite3, threading, ast
'''
    The first time the class is called, connect to the sql database
    Use thrade lock since sqlite is single thread
'''

class SQLite3:
    connector = None
    lock = threading.Lock()

    def __init__(self, file_name) -> None:
        with SQLite3.lock:
            if SQLite3.connector is None:
                SQLite3.connector = sqlite3.connect(file_name)
    
    def __enter__(self):
        with SQLite3.lock:
            self.cursor = self.connector.cursor()
            return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        with SQLite3.lock:
            self.cursor.close()

    def toObject(self, data):
        obj = {}
        for key, value in data.items():
            if isinstance(value, (int, float)):
                obj[key] = value
            else:   
                try:
                    obj[key] = ast.literal_eval(value)
                except:
                    obj[key] = value
        return obj

    def setup(self, table_name, schema):
        with self as cursor:
            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
            result = cursor.fetchone()

            # table already exists, check if the schema is the same 
            if result:
                cursor.execute(f"PRAGMA table_info({table_name})")
                existing_schema = cursor.fetchall()
                existing_schema_list = []
                for col in existing_schema:
                    column_name = col[1]
                    column_type = col[2]
                    primary_key = col[-1] == 1
                    if primary_key:
                        existing_schema_list.append(f'{column_name} {column_type} PRIMARY KEY')
                    else:
                        existing_schema_list.append(f'{column_name} {column_type}')

                # Remove leading and trailing whitespaces and split the schema string by comma
                schema_list = [col.strip() for col in schema.replace("\n", "").split(",") if col.strip()]

                # Check if the schema has changed
                if set(existing_schema_list) != set(schema_list):
                    security = input("Schema has chaned, update the database? (y/n)")
                    if (security != "y"): exit()
                    # Schema is different, update the table
                    cursor.execute(f'DROP TABLE IF EXISTS {table_name}_old')
                    cursor.execute(f"ALTER TABLE {table_name} RENAME TO {table_name}_old")
                    cursor.execute(f'CREATE TABLE {table_name} ({schema})')
                    cursor.execute(f'DROP TABLE {table_name}_old')
                    self.connector.commit()

            # table does not exist, create it
            else:
                cursor.execute(f'CREATE TABLE {table_name} ({schema})')
                self.connector.commit()
    
    # Get player from database
    def load(self, table_name, keyname, keyvalue, schema_attributes):
        with self as cursor:
            cursor.execute(f"SELECT * FROM {table_name} WHERE {keyname} = ?", (keyvalue,))
            result = cursor.fetchone()
            if result: return self.toObject(dict(zip(schema_attributes, result)))
            else: return {}

    # Save or update a record 
    def save(self, table_name, keyname, data):
        with self as cursor:
            keys = data.keys()
            values = [] # check here
            for value in data.values():
                if isinstance(value, (bool, list, dict, tuple)): values.append(str(value))
                else: values.append(value)
            values = tuple(values)
            placeholders = ','.join(['?' for _ in keys])

            query = f"""
                INSERT INTO {table_name} ({','.join(keys)}) 
                VALUES ({placeholders})
                ON CONFLICT({keyname}) DO UPDATE SET {', '.join([f'{k}=excluded.{k}' for k in keys if k != keyname])};
            """

            cursor.execute(query, values)
            self.connector.commit()

    # Remove
    def remove(self, table_name, key_name, key_value):
        with self as cursor:
            cursor.execute(f'DELETE FROM {table_name} WHERE {key_name} = ?', (key_value,))
            self.connector.commit()


    # read all the content of the table
    def readTable(self, table_name, count=-1):
        with self as cursor:
            cursor.execute(f"SELECT * FROM {table_name}")
            if count == -1:
                rows = cursor.fetchall()
            else:
                pass # TODO
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = [col[1] for col in cursor.fetchall()]
            return [dict(zip(columns, row)) for row in rows]

    def find(self, table_name, **kwargs):
        with self as cursor:
            query = f"SELECT * FROM {table_name} WHERE "
            for i, (col,val) in enumerate(kwargs.items()):
                if col not in ("db_file","table_name"):
                    if i == 0:
                        query += f" {col} = '{val}' "
                    else:
                        query += f" AND {col} = '{val}' "
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = [col[1] for col in cursor.fetchall()]
            return [dict(zip(columns, result)) for result in results]
