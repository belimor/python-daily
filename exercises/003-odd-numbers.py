#!/usr/bin/python3

# Exercise: Find Odd Nnd Even umbers

# Python program to find odd and even numbers entered by the user and add them to a list

user_numbers = input("Enter numbers separated by space: ").split()
odd_numbers = []
even_numbers = []
for n in user_numbers:
    if int(n) % 2 != 0:
        odd_numbers.append(int(n))
    if int(n) % 2 == 0:
        even_numbers.append(int(n))


print(user_numbers)
print(odd_numbers)
print(even_numbers)

