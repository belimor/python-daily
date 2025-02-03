#!/usr/bin/python3

# File operations in Python allow you to interact with files for tasks like reading, writing, appending, and modifying data

# Opening a File
file = open("example.txt", "w")
file.write("Hello World!")
file.close 
# Always close the file after use

# Writing to a file
with open("example.txt", "w") as file:
    file.write("This is the first line\n")
    file.write("This is the second line\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading Line by Line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Appending to a File
with open("example.txt", "a") as file:
    file.write("One more line\n")

# Checking if a File Exists
import os

if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File does not exist")


# Deleting a File
if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File removed")
else:
    print("File not found")

# Handling Exceptions in File Operations
try:
    with open("example.txt","r") as file:
        content = read.file()
except FileNotFoundError:
    print("File not found")
except IOError:
    print("Cant read th file")

# The pathlib module offers a modern approach:
from pathlib import Path

# Create a file and write
path = Path("example.txt")
path.write_text("Hello from pathlib!")

# Read a file
print(path.read_text())

if path.exists():
    path.unlink()
    print("File removed")



