#!/usr/bin/python3

# In Python, loops are used to execute a block of code repeatedly. 
# Python provides two main types of loops: for loop and while loop. 
# Here's a detailed overview of each type with examples.

# Iterating Over a List
fruits = ["apple","orange","banana"]
for fruit in fruits:
    print(fruit)

# Using range() in a for Loop
for i in range(5):
    print(i)

# Iterating Over a String
print("Iterating Over a String:")
for char in "hello":
    print(char)

# Using break and continue
# break: Exits the loop entirely.
# continue: Skips the rest of the loop for the current iteration.
print("Using break and continue:")
for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

# Using else with for Loop
print("Using else with for Loop:")
for i in range(5):
    print(i)
else:
    print("Finished without brake")

# while Loop
print("while Loop:")
count = 0
while count < 5:
    print(count)
    count += 1

# Using break and continue in while Loop
print("Using break and continue in while Loop")
count = 0
while count < 5:
    if count == 3:
        break # Exit the loop when count == 3
    print(count)
    count += 1

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue # Skip the rest of the code for count == 3
    print(count)

# Using else with while Loop
print("Using else with while Loop")
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Nothing")

# Nested Loops
print("Nested loops:")
for i in range(5):
    for j in range(3):
        print(i,j)

# pass
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    print(i)

# Infinite Loops
print("Infinite Loop (ctrl+c to stop):")
while True:
    pass
