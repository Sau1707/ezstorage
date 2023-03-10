# EzStorage

The goal of the package is to make it as easy as possible to load and save data for small projects.

See [Documentation](/docs/README.md) for all the technical informations.

<br />

## Example

```py
import ezstorage as ez

@ez.sqlite()
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

Create virtual enviroment:

```
python -m venv env
```

And start it:

```
source env/bin/activate # Linux
env\Scripts\activate # Window
```

If you're using visual studio code, see [this](https://stackoverflow.com/questions/56199111/visual-studio-code-cmd-error-cannot-be-loaded-because-running-scripts-is-disabl/67420296#67420296) if you get the error: `cannot be loaded because running scripts is disabled on this system`

Install the depencies

```

```

And the package as local development

```
python -m pip install --editable .
```

https://packaging.python.org/en/latest/tutorials/packaging-projects/
https://www.seanh.cc/2022/05/21/publishing-python-packages-from-github-actions/

<br />

## Planned

-   sqlite:
    -   key.uuid
-   sqlite (currently working on)
-   csv file
-   json file
-   MySQL
