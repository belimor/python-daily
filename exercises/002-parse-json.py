#!/usr/bin/python3

# Exercise: Parse a JSON File

# Write a Python program that:
# - Reads the JSON file.
# - Extracts and prints the name of the company and its location.
# - Prints the names of all employees working in the company.
# - Finds and prints the department of the employee with a specific ID

# Expected output for data.json file:

# Company: TechCorp
# Location: New York
# Employees:
# - Alice
# - Bob
# - Charlie
# Department of employee with ID 2: Engineering

import json

with open("data.json","r") as file:
    dataf = json.load(file)

print(f"Company: {dataf['company']}")
print(f"Location: {dataf['location']}")
print("Employees:")
for line in dataf['employees']:
    print(f" - {line['name']}")
    if line['id'] == 2:
        department = line['department']

print(f"Department of employee with ID 2: {department}")



