#!/usr/bin/python3

# In Python, the input() function is used to get user input from the console.

user_input = input("Enter something: ")
print(user_input)

# Convert the input to an integer using int().
age = int(input("How old are you? "))
print(f"You are {age} years old.")

# Split the input string into a list and convert each element to a number.
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]  # Convert each element to int
print(f"You entered: {numbers}")

# Convert the input to a float using float().
temperature = float(input("Enter the temperature: "))
print(f"The temperature is {temperature}°C.")

# Use a loop to ensure valid input.
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input!")
print(f"You entered: {number}")

