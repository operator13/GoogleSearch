import json
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(y)
print(y["name"])

print(y["city"])