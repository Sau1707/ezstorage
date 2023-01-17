## Reader

The reader can be used with any of the class that are decorared with an `ezstorage` decorator \
The role of the Reader it to read the content of a table and return the results

Let's consider the following example:

```py
import ezstorage as ez

@ez.sqlite()
class Demo:
    name: ez.key.str
    number: int

data = Demo(name="foo", number= 1)
data.save()
data = Demo(name="john", number= 1)
data.save()


r = ez.Reader(Demo)
all = r.readAll()
print(all)
# [Demo(name: foo, number: 1), Demo(name: john, number: 1)]
```
