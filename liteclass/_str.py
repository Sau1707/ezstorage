'''
    Overwrite the str of the class, return the attributes in a json pretty printed format
    if the user define a custom __str__ class, the keep the user one
'''
import json

def _Str(cls):
    if (cls.__str__ != object.__str__):
        return

    def new_str(self):
        value = {val: getattr(self, val) for val in self.schema_attributes}
        return json.dumps(value, indent=4)
    
    cls.__str__ = new_str