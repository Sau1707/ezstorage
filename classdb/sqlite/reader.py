class SqliteReader:
    def __init__(self, cls) -> None:
        self.table_name = cls.__name__
        for field_name, field_type in cls.__annotations__.items():
            print(field_name)
        pass