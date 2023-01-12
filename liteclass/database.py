from .constants import DEAFAULT_SCHEMA

def createSchema(annotations):
    """
        Create the schema from the types
    """
    schema = ""
    for field_name, field_type in annotations.items():
        schema += f"{field_name} {DEAFAULT_SCHEMA[field_type]}, \n"
    return schema.rstrip().rstrip(",")

# Create a table in the database
def setup(connector, table_name, schema):
    cursor = connector.cursor()
    # check if table already exists
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    result = cursor.fetchone()
    if result:
        # table already exists, check if the schema is the same
        cursor.execute(f"PRAGMA table_info({table_name})")
        existing_schema = cursor.fetchall()
        existing_schema_str = ' '.join([f'{col[1]} {col[2]} ,' if col[-1] != 1 else f'{col[1]} {col[2]} PRIMARY KEY,' for col in existing_schema])
        existing_schema_list = [i.strip() for i in existing_schema_str.split(",") if i != ""]
        schema_list = [i.strip() for i in schema.replace("\n", "").split(",") if i != ""]
        if set(existing_schema_list) != set(schema_list):
            security = input("Schema has chaned, update the database? (y/n)")
            if (security != "y"): exit()
            # schema is different, update the table
            cursor.execute(f"ALTER TABLE {table_name} RENAME TO {table_name}_old")
            cursor.execute(f'CREATE TABLE {table_name} ({schema})')
            cursor.execute(f'DROP TABLE {table_name}_old')
            connector.commit()
    else:
        # table does not exist, create it
        cursor.execute(f'CREATE TABLE {table_name} ({schema})')
        connector.commit()
    cursor.close()