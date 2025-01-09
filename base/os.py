#!/usr/bin/python3

# The Python os module provides a way 
# to interact with the operating system, 
# allowing you to work with files, directories, 
# environment variables, and more. 

import os

## Working with directories

# Get the current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# Change directory
os.chdir('/tmp')
print(f"Changed working directory to: {os.getcwd()}")

# Create directory
os.mkdir('example')

# List files in a directory
files = os.listdir('.')
for file in files:
    if file == 'example':
        print(f"New file in the curent directory: {file}")

# Delete directory
os.rmdir('example')

os.chdir(cwd)

## File operations

# Create an empty file
fd = os.open('example.txt', os.O_CREAT | os.O_WRONLY)
os.close(fd)

# Check if file exist
if os.path.exists('example.txt'):
    print("True")
elif os.path.isdir('example.txt'):
    print("DirTrue")

# Rename file
os.rename('example.txt','exmpl.txt')

# Remove file
os.remove('exmpl.txt')

# Get environment variable
path = os.getenv('PATH')
print(f"PATH: {path}")

# Set environment variable
os.environ['MY_VAR'] = 'my_val'
print(f"MY_VAR : {os.getenv('MY_VAR')}")

# Get name of the OS 
print(f"OS Name: {os.name}")

# Run system command
os.system('cat /etc/*release* | grep NAME')

# Join path
path = os.path.join('/tmp', 'example.txt')
print(f"File path: {path}")










