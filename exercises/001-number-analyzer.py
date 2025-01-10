#!/usr/bin/python3

# Exercise: Number Analyzer

# Asks the user to input a list of numbers separated by spaces.
# Converts the input into a list of integers.
# Uses a loop to:
# - Calculate the sum of all numbers.
# - Find the largest number.
# - Count how many numbers are greater than 10.
# - Finally, print the results.

# Input:
#   Enter numbers: 5 12 7 18 3
# Result:
#   Sum of numbers: 45
#   Largest number: 18
#   Count of numbers greater than 10: 2


# Possible solution

numbers = input("Enter list of numbers separated by spaces: ").split()
print(numbers)

# Calculate the sum of all numbers:
sum = 0
for n in numbers:
    sum = sum + int(n)
print(f"Sum of numbers: {sum}")

# Find the largest number
lnum = 0
for n in numbers:
    if lnum < int(n):
        lnum = int(n)
print(f"Largest number: {lnum}")

# Count of numbers greater than 10
count = 0
for n in numbers:
    if int(n) > 10:
        count += 1
print(f"Count of numbers greater than 10: {count}")


# Better solution

user_input = input(f"Enter numbers separated by spaces: ")
numbers = [int(n) for n in user_input.split()]
sum = 0
lnum = float('-inf') # Smallest possible value as a starting point
count = 0

for n in numbers:
    sum += n
    if n > lnum: lnum = n
    if n > 10: count += 1

print(f"Sum of numbers: {sum}")
print(f"Largest number: {lnum}")
print(f"Count of numbers greater than 10: {count}")


