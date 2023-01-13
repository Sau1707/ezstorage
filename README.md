# Class db

A python package to ealy handle a sql database data colum

## Getting started

Import sqlite decorator and key object

```python
from classdb.sqlite import sqlite
from classdb import key
```

Create a class with that decorator

```python
@sqlite()
class Demo:
    key: key.str
    number: int
    lista: list
```

You can pass the filename as a props to the decorator

```python
@sqlite("file.db")
```

Note:

-   By default the name is `data.db`
-   Currenty only sqlite is supported
-   The class name will be the same as the database table
-   The keys name will the the same as the database colums

<br />

## Types

Each type map to a database type:

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

Note:

-   If can be only a single key
-   `list, dict, tuple` are converted to string to save them
-   The database schema is checked the first time a class is initialized

<br />

## Usage

To create a record in the table Demo (if no table exist, it will create one)

```python
d = Demo(key="10", number=10, lista=[1,2,3])
```

To modify and save the data

```py
d.number = 20
d.lista = [2,3,4]
d.save()
```
