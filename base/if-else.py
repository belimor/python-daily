#!/usr/bin/python3

# The if...else statement in Python is used for conditional execution based on whether a condition evaluates to True or False.

x = 10
if x > 5:
    print(f"{x} > 5")
else:
    print(f"{x} is not grater than 5")

# if...elif...else
x = 10
if x < 10:
    print("x < 10")
elif x == 10:
    print("x = 10")
else:
    print("x is grater than 10")

# Nested if...else
x = 15
if x > 10:
    if x % 2 == 0:
        print("x is greater than 10 and even")
    else:
        print("x is greater than 10 and odd")
else:
    print("x is 10 or less")

# One-Line if...else (Ternary Operator)
x = 5
result = "Even" if x % 2 == 0 else "Odd"
print(result)

# Multiple Conditions with Logical Operators
age = 25
has_id = True
if age > 18 and has_id:
    print("You can enter the club.")
else:
    print("You cannot enter the club.")




