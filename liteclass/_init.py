'''
    Overwrite the init of the class
'''

# The init take as parametr the database name

class NewInit:
    def __init__(self, cls, *args, **kwargs) -> None:
        original_init = cls.__init__

        def new_init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)

        cls.__init__ = new_init