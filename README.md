# Class db

The goal of the package is to make it as easy as possible to load and save data for small projects.

See [Documentation](/docs/README.md) for all the technical informations.

<br />

## Example

```py
from classdb import key
from classdb.sqlite import sqlitedb, SqliteReader

@sqlitedb()
class Demo:
    name: key.str
    number: int

data = Demo(name="john", number= 1)
print(data) # Demo(name: john, number: 1)

data.number = 10
print(data) # Demo(name: john, number: 10)

print(data.match()) # False
data.save()
print(data.match()) # True
```

<br />

## Development:

Install the package as local development

```
python -m pip install --editable .
```

TODO: Create env and requirements
https://packaging.python.org/en/latest/tutorials/packaging-projects/
https://www.seanh.cc/2022/05/21/publishing-python-packages-from-github-actions/

<br />

## Planned

-   sqlite (currently working on)
-   csv file
-   json file
-   MySQL
