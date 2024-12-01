#!/usr/bin/python3

# List comprehensions in Python are a concise way to create lists 
# by iterating over an iterable and optionally filtering elements. 
# They can often replace traditional for loops used to populate a list 
# and make the code more readable and efficient.

# [expression for item in iterable if condition]

# Create a list of squares:
squares = [x**2 for x in range(10)]
print(squares)

# Filter even numbers:
evens = [x for x in range(10) if x%2 == 0]
print(evens)

# Apply a function to each element:
uppercase = [char.upper() for char in 'hello']
print(uppercase)

# Nested loops:
pairs = [(x,y) for x in range(3) for y in range(3)]
print(pairs)

# Use with conditions:
f_sq = [x**2 for x in range(10) if x%2 == 0]
print(f_sq)

# Flatten a nested list:
nested_list = [[1, 2], [3, 4], [5, 6]]
flttnd = [item for sublist in nested_list for item in sublist]
print(flttnd)





