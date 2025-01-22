#!/usr/bin/python3

# Task:
# Given an integer, n, perform the following conditional actions:

# If is odd, print W
# If is even and in the inclusive range of 2 to 5 print NW
# If is even and in the inclusive range of 6 to 30 print W
# If is even and greater than 30 print NW

n = int(input("Input number:").strip())

if (n % 2) != 0:
    my_string = "W"
else:
    if n >= 2 and n <= 5:
        my_string = "NW"
    if n >= 6 and n <= 30:
        my_string = "W"
    if n > 30:
        my_string = "NW"

print(my_string)
