# Sqlite

Usefull to ealy read, write, edit and seach data in a sqlite database

<br />

## Get started

import `classdb.sqlite`

```ps
from classdb.sqlite import sqlitedb
```

`sqlitedb` is a python decorator for a class and can be use as follow:

```ps
@sqlitedb()
class Demo:
    name: key.str
    number: int
```

In this case we refer to a table `Demo` with 2 colums, key and number.

> See [TYPES](TYPES.md) for details about types

<br />

The database name can be passed as a props

```py
@sqlitedb("file.db")
```

If no database is passed, the default one will be used `data.db`

<br />

## Usage

Once the class defined, it can be use as follow

```py
data = Demo(name="example", number= 100)
print(data) # Demo(name: example, number: 100)
data.save()
```

This will create a entry in the database, with key: "example" and number: 100.

<center>

|  Name   | Number |
| :-----: | :----: |
| example |  100   |

</center>

| Syntax    | Description |   Test Text |
| :-------- | :---------: | ----------: |
| Header    |    Title    | Here's this |
| Paragraph |    Text     |    And more |

</center>

> Note: The first time the class is initiated, it will check that the database structure it's the correct one, if the table don't exist it will create one and if the table has a diffrent schema it will be update to match the class types.

<br />

After that the data can be used and modifed like a normal object and can be saved at any time with the `save()` method.

```py
data.number = 200
data.save()
```

If a entry in the database alreay exist, can be get as follow:

```
data = Demo("example")
```
