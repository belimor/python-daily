#!/usr/bin/python3

import json

json_data = '{"name": "John", "age": "35", "city": "Toronto"}'

# Convert json string to python dictionary
data = json.loads(json_data) 
print(data)

# Read json file and convert to dictionary
with open('data.json','r') as file:
    dataf = json.load(file)
print(dataf)

print(data['name'])
data['age'] = 33
data['gender'] = 'Male'
del data['city']

json_string = json.dumps(data, indent=4)
print(json_string)

with open('data.json','w') as file:
    json.dump(dataf, file, indent=4)


