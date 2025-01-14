#!/usr/bin/python3

# A tuple in Python is an immutable, ordered collection of items. 
# Unlike lists, tuples cannot be modified after creation, 
# making them useful for storing fixed data.

# Key Features of Tuples:
# - Ordered: Items have a defined order.
# - Immutable: Cannot change their contents (add, remove, or modify items).
# - Heterogeneous: Can contain elements of different data types.
# - Indexable: Items can be accessed via an index.

my_tuple = (1, 2, 3, 4)
mixed = (1, "text", 6, True)
single = (42,)
test = (42)

print(my_tuple)
print(single)
print(type(single))
print(test)
print(type(test))

# Accessing Tuple Elements
my_tuple=("apple","banana","orange")
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])

# Tuple Packing and Unpacking
packed = ("John", 25, "Developer")
name, age, profession = packed
print(name, age, profession)

# Slicing Tuples
my_tuple = (10, 20, 30, 40, 50, 60)
print(my_tuple[1:3])

immutable = (1, 2, 3)
# immutable[1] = 5  # Raises TypeError

# Operations on Tuples
tuple1 = (1,2)
tuple2 = (3,4)
print(tuple1 + tuple2)
print(tuple1 * 3)
print(1 in tuple1)

# Nested Tuples
nested_tuples=(1,2,(3,4,5),6)
print(nested_tuples[1])
print(nested_tuples[2][0])

# Tuple Methods
mt = (10,20,30,10,30)
# count: Returns the number of occurrences of a value
print(mt.count(10))
# # index: Returns the first index of a value
print(mt.index(30))





