#!/usr/bin/python3

import os

# Read the environment variable
my_var = os.getenv("SHELL")

# Check if the environment variable exists
if my_var:
    print("Environment variable SHELL set to:", my_var)
else:
    print("SHELL is not set")
