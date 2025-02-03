#!/usr/bin/python3

# The range() function in Python generates a sequence of numbers and is commonly used in loops. 

# range(start, stop, step)
# - start (optional): The starting number of the sequence (default is 0).
# - stop: The endpoint of the sequence (exclusive).
# - step (optional): The difference between each number in the sequence (default is 1).

for i in range(3):
    print(i)
print("= = =")

for i in range(3,5):
    print(i)
print("= = =")

for i in range(1,11,2):
    print(i)
print("= = =")

for i in range(5,1,-1):
    print(i)
print("= = =")

numbers = list(range(5))
print(numbers)
print("= = =")

squares = [x**2 for x in range(5)]
print(squares)


