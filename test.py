import time
from ezstorage import key, Sqlite, Table

db = Sqlite('test.db')

@db.useTable("table_name")
class User(Table):
    age: int
    name: str
    ugfu: str


db.create_table(User)
# db.create_tables()

print(User.__schema__)

db.update_table(User)

db.drop_table(User)
# db.drop_tables()


# Make a benchmark for the table creation
# start_time = time.time()
# for i in range(1_000_000):
#     User(name='John', age=25)
# end_time = time.time()

# 1.0884144306182861
# 1.1030092239379883
# 1.1229956150054932s
# print(end_time - start_time)
