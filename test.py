import time
from ezstorage import Sqlite, Table

db = Sqlite('test.db')

@db.useTable("table_name")
class User(Table):
    age: int
    name: str
    test: str = "test"


db.create_table(User)
# db.create_tables()
# db.update_table(User)
# db.drop_table(User)
# db.drop_tables()


# user = User(name='John', age=25)
# user.save()

User.where(c for c in User if c.age > 25) 



# Make a benchmark for the table creation
start_time = time.time()
for i in range(1_000_000):
    user = User(name='John', age=25)
    user.save()

db.commit()
    
end_time = time.time()
print(end_time - start_time)



