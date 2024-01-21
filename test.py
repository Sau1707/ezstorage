from typing import dataclass_transform



@dataclass_transform()
def create_model(cls):
    cls.__init__ = ...
    cls.__eq__ = ...
    cls.__ne__ = ...
    return cls


# The create_model decorator can now be used to create new model classes:
@create_model
class CustomerModel:
    id: int
    name: str

c = CustomerModel(id=1, name="John")
