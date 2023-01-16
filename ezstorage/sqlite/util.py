from ..costants import DEAFAULT_SCHEMA, DEAFAULT_VALUES

# Create the schema from the types
def createSchema(annotations):
    schema = ""
    for field_name, field_type in annotations.items():
        schema += f"{field_name} {DEAFAULT_SCHEMA[field_type]}, \n"
    return schema.rstrip().rstrip(",")

# Return the default value for a given type
def getDefaultValue(field_type):
    default_value = DEAFAULT_VALUES.get(field_type)
    if default_value is None: 
        raise ValueError(f"Unsupported field type {field_type}")
    return default_value