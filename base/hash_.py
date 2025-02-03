#!/usr/bin/python3

# A hash function is a critical component of a hash table. 
# It maps keys to specific indexes in a table where their associated values are stored. 
# In Python, hash tables are implemented using dictionaries (dict) or sets, 
# as both are backed by hash tables.

# Key Concepts in Hash Tables
# Hash Function: Converts a key into an index within a fixed-size table.
# Collision: Occurs when two keys are mapped to the same index.
# Resolution: Collisions are handled using techniques like chaining or open addressing.

# Python's Built-In hash() Function
# The hash() function in Python returns the hash value of an object 
# (e.g., integers, strings, or tuples). 
# Custom objects can implement the __hash__() method.

print(hash("apple"))  # Output: A unique integer hash value for "apple"
print(hash(42))       # Output: Hash value for the integer 42

# Using Python's Built-in Dictionary
# In most cases, you don’t need to implement a hash table manually 
# because Python’s dict already provides an efficient hash table implementation.

hash_table = {}
hash_table["apple"] = 5
hash_table["banana"] = 10
hash_table["grape"] = 15

print(hash_table)
print(hash_table["apple"])   # Output: 5
print(hash_table.get("banana"))  # Output: 10

del hash_table["banana"]
print(hash_table.get("banana"))  # Output: None

# Python’s dictionaries are optimized for performance and handle collisions internally. 
# Use them unless you need a custom implementation for educational purposes or special requirements.


