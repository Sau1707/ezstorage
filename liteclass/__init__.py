from ._init import _Init
from ._str import _Str
from .constants import PrimaryKey

def Tableclass(db="data.db"):

    def decorator(cls):
        _Init(cls, db)
        _Str(cls)

        return cls 
    return decorator
        