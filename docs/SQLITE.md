# Sqlite

Usefull to ealy read, write, edit and seach data in a sqlite database

## Table of contents

-   [Get started](#get-started)
-   [Usage](#usage)
    -   [Save](#save)
    -   [Remove](#remove)
    -   [Match](#match)
    -   [Load](#load)

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

|     |  Name   | Number |
| :-: | :-----: | :----: |
| #1  | example |  100   |

> Note: The first time the class is initiated, it will check that the database structure it's the correct one, if the table don't exist it will create one and if the table has a diffrent schema it will be update to match the class types.

If a entry in the database alreay exist, can be get by passing it's key:

```py
data = Demo("example")
print(data) # Demo(name: example, number: 200)
```

<br />

### Save

After that the data can be used and modifed like a normal object and can be saved at any time with the `save()` method.

```py
data.number = 200
print(data) # Demo(name: example, number: 200)
data.save()
print(data) # Demo(name: example, number: 200)
```

|     |  Name   | Number |
| :-: | :-----: | :----: |
| #1  | example |  200   |

<br />

### Remove

To remove an entry, there is the `remove()` function:

```py
data = Demo("example")
print(data) # Demo(name: example, number: 200)
data.remove()

data = Demo("example")
print(data) # Demo(name: example, number: 0)
```

<br />

### Match

It is possible to check if the current class state and the database are the same:

```py
data = Demo(name="john", number= 1)
print(data) # Demo(name: john, number: 1)
print(data.match()) # False
data.save()
print(data.match()) # True
```

> The `match()` function keep track of when the class make operations, if an exernal operation is done to the database or from another class connected to the same row this method could break.

<br />

### Load

To update a class use the `load()`

```py
data = Demo(name="john", number= 1)
data.save()
data.number = 10
print(data) # Demo(name: john, number: 10)
data.load()
print(data) # Demo(name: john, number: 1)
```

In this case the number has been updated but the class was not saved into the database. The load operation loaded the entry of the database and overwrite the class attributes

<br />

## Reader
