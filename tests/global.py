import ezstorage as ez

@ez.sqlite()
class Demo:
    name: ez.key.str
    number: int

data = Demo(name="foo", number= 1)
data.save()

print(data["name"])


r = ez.Reader(Demo)
all = r.readAll()
print(all)