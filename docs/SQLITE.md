# Sqlite

Usefull to ealy read, write, edit and seach data in a sqlite database

## Get started

import `sqlitedb`

```ps
from classdb.sqlite import sqlitedb
```

`sqlitedb` is a python decorator for a class and can be use as follow:

```ps
@sqlitedb()
class Demo:
    key: key.str
    number: int
```

In this case we refere to a table `Demo` with 2 colums, key and number.

See [TYPES](TYPES.md) for details about types

The database name can be passed as a props

```py
@sqlitedb("file.db")
```

if no database is passed, the default one will be used `data.db`

## Usage

Once the class defined, it can be use as follow

```py
data = Demo(key="example", number: 100)
```

The first time the class is initiated, it will check that the database structure it's the correct one, if the table don't exist it will create one and if the table has a diffrent schema it will be update to match the class types.

After that the data can be used and modifed like a normal object

```py
data.number = 200
```
