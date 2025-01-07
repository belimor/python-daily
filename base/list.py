#!/usr/bin/python3

# Lists are ordered, mutable (can be changed), 
# and can hold items of different types (e.g., integers, strings, objects).

empty_list = []
numbers = [1,2,3,4,5]
strings = ["apple","orange","banana"]
mixed = [1,2,3,"apple","cherry"]
nested = [[1,2],[3,4],[5,6]]

print(numbers, nested)
print(strings[1],mixed[-1])

print(strings)
strings[1] = "blueberry"
strings.append("peach")
strings.insert(1,"mango")
strings.remove("banana")
print(strings)
del strings[0]
last = strings.pop()
print(last)
print(strings)

for s in strings:
    print(s)
print("mango" in strings)
print(numbers)
print(numbers[1:4])
print(numbers[::-1])

# Generate a list of squares
squares = [x ** 2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

numbers = [5, 2, 9, 1]
numbers.sort()  # Sort in ascending order
print(numbers)  # Output: [1, 2, 5, 9]

numbers.sort(reverse=True)  # Sort in descending order
print(numbers)  # Output: [9, 5, 2, 1]



