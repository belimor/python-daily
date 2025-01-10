#!/usr/bin/python3

# In Python, a dictionary is a mutable, unordered collection of key-value pairs. 
# Each key is unique, and the values can be of any data type.

# Create e,pty dictionary
captaines = {}
cap = dict()

data = {"name": "Alice", "age": 25, "city": "New York"}
print(data['name'])
print(data.get("gender","Not Found"))

data['age']=33
data['gender'] = 'Female'
age = data.pop("age")
print(age)
print(data)

last_inserted_item = data.popitem()
print(last_inserted_item)
print(data)

for key in data:
    print(key)

for value in data.values():
    print(value)

for key,value in data.items():
    print(f"{key}: {value}")
