# Sqlite

Usefull to ealy read, write, edit and seach data in a sqlite database

<br />

## Table of contents

-   [Get started](#get-started)
-   [Usage](#usage)
    -   [Save](#save)
    -   [Remove](#remove)
    -   [Match](#match)
    -   [Load](#load)
-   [Reader](#reader)

<br />

## Get started

```py
import ezstorage as ez
```

`ez.sqlite()` is a python decorator for a class and can be use as follow:

```py
@ez.sqlite()
class Demo:
    t_key: ez.key.str
    # or t_key: ez.key.int
    t_number: int
    t_decimal: float
    t_string: str
    t_truth: bool
    t_array: list
    t_object: dict
    t_group: tuple
```

Where the name of the class rappresent the database table name and the attribures it's a column in that table. Each attribure has a specific type in the sqlite database, if a type doesn't exist it will be stored as string and converted back when the data is loaded

```python
- int: INTEGER
- float: REAL
- str: TEXT
- bool: INTEGER
- list: TEXT
- dict: TEXT
- tuple: TEXT
- key.int: INTEGER PRIMARY KEY
- key.str: TEXT PRIMARY KEY
```

The database name can be passed as a props

```py
@ez.sqlite("file.db")
```

If no database is passed, the default one will be used `data.db`

> Note: The first time the class is initiated, it will check that the database structure it's the correct one, if the table don't exist it will create one and if the table has a diffrent schema it will be update to match the class types.

> Note: Database migration are planned but not implemented yet. By changing the table it will erase the entire content.

<br />

## Usage

Let's consider an example

```py
@ez.sqlite()
class Demo:
    name: ez.key.str
    number: int
```

Once the class defined, it can be use as follow

```py
data = Demo(name="example", number= 100)
print(data) # Demo(name: example, number: 100)
data.save()
```

This will create a entry in the table "Demo", with key: "example" and number: 100.

|     |  Name   | Number |
| :-: | :-----: | :----: |
| #1  | example |  100   |

>

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
