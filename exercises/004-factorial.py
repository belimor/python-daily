#!/usr/bin/python3

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Solution 1

def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)

uinput = int(input("Enter number between 10 and 1: "))
print(factorial(uinput))

# Solution 2

user_in = input("Enter number between 10 and 1: ")
i = int(user_in)
factorial = 1
sequence = []
while i > 0:
    factorial = factorial * i
    sequence.append(i)
    i -= 1

print(sequence)
print(factorial)
